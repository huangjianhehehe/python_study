import pandas as pd
from datetime import date,timedelta

# 计算月份+1的算法
def add_month(d,md):
	yd = md//12
	m=d.month+md%12
	if m!=12:
		yd+=m//12
		m=m%12
	return date(d.year+yd,m,d.day)


books = pd.read_excel('E:/python_xls/Books.xlsx',skiprows=3,usecols="C:F",index_col=None,dtype={'ID':str,'InStore':str,'Date':str})

start = date(2020,1,1)

for i in books.index:
	#books['ID'].at[i]=i+1  与下面一行等价
	books.at[i,'ID']=i+1
	books['InStore'].at[i]='Yes' if i%2==0 else 'No'
	#books['Date'].at[i]=start+timedelta(days=i)  # 加天数
	#books['Date'].at[i]=date(start.year+i,start.month,start.day)  # 加年份
	books['Date'].at[i]=add_month(start,i)  # 加月份

books.set_index('ID',inplace=True)  # 去掉默认索引

print(books)

books.to_excel('E:/python_xls/books2.xlsx')

print('Done!')