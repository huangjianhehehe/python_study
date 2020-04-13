import keyboard
import time
from PIL import ImageGrab # 引入剪切板

from aip import AipOcr

class RecGt(object):

	def __init__(self):
		""" 你的 APPID AK SK """
		self.APP_ID = '19387667'
		self.API_KEY = 'XIC5SNSR6npc95LOIanGSdHL'
		self.SECRET_KEY = 'LjrXDtObeVAlsgmSk3KT6tS60GRCFmf1'

		self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)


		self.filepath = r'e:\python_xls\文字识别\test.png'  # r在这里是防止转义
	def screenshot(self):
		if not keyboard.wait(hotkey='f1'):     # 如果按下了F1,并且 再按下了enter,ctrl+c有点问题
			if not keyboard.wait(hotkey='enter'):
				time.sleep(0.01)  # 延时0.01
				image = ImageGrab.grabclipboard() # 放入剪切板
				image.save('test.png')


	def reg(self):
		f=open(self.filepath, 'rb')

		image = f.read()

		f.close()

		""" 调用通用文字识别, 图片参数为本地图片 """
		req = self.client.basicGeneral(image);
		print(req)

		all_text = ''
		for i in req['words_result']:
			all_text += i['words'] + '\n'

		print(all_text)

# 调用
re =RecGt()
re.screenshot()
re.reg()
