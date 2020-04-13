from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '19387667'
API_KEY = 'XIC5SNSR6npc95LOIanGSdHL'
SECRET_KEY ='LjrXDtObeVAlsgmSk3KT6tS60GRCFmf1'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filepath = r'e:\python_xls\文字识别\test.png'  # r在这里是防止转义

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(filepath)

""" 调用通用文字识别, 图片参数为本地图片 """
req = client.basicGeneral(image);
print(req)

all_text=''
for i in req['words_result']:
	all_text +=i['words']+'\n'

print(all_text)
