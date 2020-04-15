import  pandas as pd

students= pd.read_excel('./Students_name.xlsx')

dupe = students.duplicated(subset='Name') # 以名字查询重复

print(students)
print(students.iloc[dupe.index])
