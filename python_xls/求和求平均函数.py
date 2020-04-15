import  pandas as pd

students = pd.read_excel('./Students_score.xlsx',index_col='ID')

temp = students[['Test_1','Test_2','Test_3']]
row_sum = temp.sum(axis=1)  #从左到右求和
row_mean = temp.mean(axis=1)   #求平均

students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1','Test_2','Test_3','Total','Average']].mean()   # 对所有求平均
col_mean['Name']='Summary'

# 添加一行,忽略索引
students = students.append(col_mean,ignore_index=True)

print(students)