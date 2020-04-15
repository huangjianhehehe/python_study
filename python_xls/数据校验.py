import  pandas as pd


# print(students)

def Qty_validation(row):
	try:
		assert row.Qty==20 # 使用断言,也可以用if
	except:
		print(f'zj_data{row.Procuct_Id}has an invalid Pty{row.Qty}.')

zj_data = pd.read_excel('./4列.xlsx')

zj_data.apply(Qty_validation,axis=1)  # axis=1 表示从左向右