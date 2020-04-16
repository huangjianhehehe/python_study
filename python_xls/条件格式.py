import  pandas as pd


def low_socre_red(s):
	color = 'red' if s<60 else 'black'
	return  f'color:{color}'

def highest_score_green(col):
	return ['background']

students = pd.read_excel(r'./Students_score.xlsx')

students.style.applymap(low_socre_red,subset=['Test_1','Test_2','Test_3'])

students.to_excel(r'./students_score_format.xlsx')