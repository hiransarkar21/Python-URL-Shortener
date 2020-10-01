import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyshorteners

Font = QFont()
Font.setWordSpacing(2)
Font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

		self.window_configuration()
		self.user_interface()

	def window_configuration(self):
		
		self.setFixedHeight(470)
		self.setFixedWidth(500)
		self.setFont(Font)
		self.setWindowTitle("Python URL Shortener".center(25))
		self.setWindowIcon(QIcon("shlink-logo-blue.ico"))

	def user_interface(self):
		
		application_title = QLabel(self)
		application_title.setText("Python URL Shortener")
		application_title.move(155, 100)
		application_title.setStyleSheet("font-size: 17px; font-family: calibri; font-weight: light;")

		self.get_original_link = QLineEdit(self)
		self.get_original_link.resize(250, 35)
		self.get_original_link.move(120 , 200)
		self.get_original_link.setStyleSheet("border: 1.5px solid; border-radius: 3px; padding-left: 10px; padding-right: 10px; font-size: 16px; font-family: calibri; font-weight: light;")

		self.process_link_button = QPushButton(self)
		self.process_link_button.setText("Generate Link")
		self.process_link_button.resize(150, 40)
		self.process_link_button.move(170, 270)
		self.process_link_button.setStyleSheet("background-color: black; color: white; border-radius: 4px; font-size: 17px; font-weight: light; padding-right: 7px; padding-left: 7px; font-family: calibri;")
		self.process_link_button.clicked.connect(self.shorten_link)

		footer = QLabel(self)
		footer.setText("Powered By Python and PyQt5")
		footer.move(160, 420)
		footer.setStyleSheet("font-size: 10px; ")

	def shorten_link(self):

		initial_link = self.get_original_link.text()
		customized_link = pyshorteners.Shortener().tinyurl.short(initial_link)
		QApplication.clipboard().setText(str(customized_link))

		self.timer = QTimer(self)
		self.timer.setInterval(3000)
		self.timer.timeout.connect(self.back_to_main)

		self.process_link_button.setText("Link Copied")
		self.timer.start()

	def back_to_main(self):

		self.get_original_link.setText("")
		self.process_link_button.setText("Generate Link")
		self.timer.stop()

application = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(application.exec_())