import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget ,QToolTip,QPushButton,QHBoxLayout ,QWidget#窗口居中
from PyQt5.QtGui import QIcon,QFont

class ToolTips(QMainWindow):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# 设置主窗口标题
		self.setWindowTitle('设置控件提示信息')

		# 设置窗口尺寸
		self.setGeometry(300,300,200,300)

		# 控件提示信息设置
		QToolTip.setFont(QFont('SansSerif',12))
		self.setToolTip('今天是<b>星期五</b>')

		self.button1 = QPushButton('我的按钮')
		self.button1.setToolTip('这是一个按钮,Are You ok?')
		layout = QHBoxLayout()
		layout.addWidget(self.button1)

		mainFrame = QWidget()
		mainFrame.setLayout(layout)  # 设置布局
		self.setCentralWidget(mainFrame)



if __name__ =='__main__':
	app=QApplication(sys.argv)

	app.setWindowIcon(QIcon('../images/qq.ico'))
	main = ToolTips()
	main.show()

	sys.exit(app.exec_())
