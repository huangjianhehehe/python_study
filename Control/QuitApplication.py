import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QPushButton,QHBoxLayout,QWidget #窗口居中
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):

	def __init__(self,parent=None):
		super(QuitApplication,self).__init__(parent)

		# 设置主窗口标题
		self.setWindowTitle('第一个主窗口应用')

		# 设置窗口尺寸
		self.resize(400,300)

		# 添加button
		self.button1 = QPushButton('退出应用程序')

		# 将信号与槽关联
		self.button1.clicked.connect(self.onClick_Button)

		layout = QHBoxLayout()

		layout.addWidget(self.button1)

		mainFrame = QWidget()

		mainFrame.setLayout(layout)
		self.setCentralWidget(mainFrame)

	def onClick_Button(self):
		sender = self.sender()
		print(sender.text() + '按钮被按下')
		app = QApplication.instance()
		app.quit()

if __name__ =='__main__':
	app=QApplication(sys.argv)

	app.setWindowIcon(QIcon('../images/qq.ico'))
	main = QuitApplication()
	main.show()

	sys.exit(app.exec_())






