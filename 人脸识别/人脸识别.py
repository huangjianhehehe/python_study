import sys

import cv2
import  face_recognition  # 人脸识别库

face_image = face_recognition.load_image_file(r'e:\python_study\人脸识别\8.png')

#print(face_image)
# print(type(face_image)) # 这是一个多维数组

face_encodings=face_recognition.face_encodings(face_image)
# 给定图像，返回图像每个面的128维人脸编码，进行特征提取
#print(face_encoding)

# 给定图像，返回图像中每个人脸的面部特征位置
face_locations=face_recognition.face_locations(face_image)
print(face_locations)  # 每个元组保存上，右，下，左 四个坐标像素位

n=len(face_encodings)  # 判断当前图像人脸个数
# print(n)

if n>2:
	print('超出2个人')
	sys.exit()
try:
	face1 = face_encodings[0]
	face2 = face_encodings[1]
except:
	print('2')
	sys.exit()

# 两个人脸如何比较
result= face_recognition.compare_faces([face1],face2,tolerance=0.5) #tolerance参数超低，精度高

print(result)

# 完成框图
if result == [True]:
	print('1')
	name='PASS'  # 如果一致
else:
	print('0')
	name='No'
# 绘图
for i in range(len(face_encodings)):
	face_encoding=face_encodings[(i-1)]
	face_location=face_locations[(i-1)]
	print(face_locations)
	top,right,bottom,left =face_location # 定义坐标

	# 画框          图像             坐标                 颜色   粗细
	cv2.rectangle(face_image,(left,top),(right,bottom),(0,255,0),2)

	cv2.putText(face_image,name,(left-10,top-10), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),2)

# 颜色
face_image_rgb = cv2.cvtColor(face_image,cv2.COLOR_BGR2RGB)

# 展示图像
cv2.imshow('Output',face_image_rgb)

# 保存图像
cv2.imwrite(r'f:/bj/intrest.jpg',face_image_rgb,[int(cv2.IMWRITE_JPEG_QUALITY),100])

# 等待关闭
cv2.waitKey(0)

