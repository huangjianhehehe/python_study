import  sys
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPalette,QPixmap,QIcon
from PyQt5.QtCore import Qt


class LableDemo(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		label1 = QLabel(self)
		label2 = QLabel(self)
		label3 = QLabel(self)
		label4 = QLabel(self)

		label1.setText('<font color=yellow>这是一个文本标签</font>') # 定义一个label,字体黄颜色
		label1.setAutoFillBackground(True)
		palette = QPalette()
		palette.setColor(QPalette.Window,Qt.blue)
		label1.setPalette(palette)
		label1.setAlignment(Qt.AlignCenter)

		label2.setText("<a href='#'>欢迎使用Python PyQt5 </a>")

		label3.setAlignment(Qt.AlignCenter)
		label3.setToolTip('这是一个图片标签')
		label3.setPixmap(QPixmap('../images/nainai.jpg'))
		label3.setBaseSize(300,200)
		label3.setScaledContents(True)

		label4.setOpenExternalLinks(True)
		label4.setText("<a href='http://www.baidu.com'>欢迎前来查询</a>")
		label4.setAlignment(Qt.AlignRight)
		label4.setToolTip('这是一个链接')

		vbox = QVBoxLayout()
		vbox.addWidget(label1)
		vbox.addWidget(label2)
		vbox.addWidget(label3)
		vbox.addWidget(label4)

		label2.linkHovered.connect(self.linkHovered)

		label4.linkActivated.connect(self.linkClicked)

		self.setLayout(vbox)
		self.setWindowTitle('这是一个Label示例')


	def linkHovered(self):
		print('当鼠标没过label2标签时触发事件')

	def linkClicked(self):

		print('当鼠标点击label4标签时触发事件')

if __name__ =='__main__':
	app=QApplication(sys.argv)

	app.setWindowIcon(QIcon('../images/qq.ico'))
	main = LableDemo()
	main.show()

	sys.exit(app.exec_())

