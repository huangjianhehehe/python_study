import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget  #窗口居中
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):

	def __init__(self,parent=None):
		super(CenterForm,self).__init__(parent)

		# 设置主窗口标题
		self.setWindowTitle('第一个主窗口应用')

		# 设置窗口尺寸
		self.resize(400,300)
		self.center()

	def center(self):
		#获取屏幕坐标系
		screen = QDesktopWidget().screenGeometry()
		#获取窗口坐标系
		newLeft = (screen.width()-self.width())/2
		newRight = (screen.height()-self.height())/2
		self.move(newLeft,newRight)



if __name__ =='__main__':
	app=QApplication(sys.argv)

	app.setWindowIcon(QIcon('../images/qq.ico'))
	main = CenterForm()
	main.show()

	sys.exit(app.exec_())
