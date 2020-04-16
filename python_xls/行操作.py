import  pandas as pd

page_001 = pd.read_excel(r'./Students_Score.xlsx',sheet_name='Page_001')

page_002 = pd.read_excel(r'./Students_Score.xlsx',sheet_name='Page_002')

# 两个工作表合并
students = page_001.append(page_002).reset_index(drop=True)  # 把002追加到001中,原索引删除

# 追 加数据
stu = pd.Series({'ID':41,'Name':'Abel','score':99})
students= students.append(stu,ignore_index=True)

# 更改数据
stu = pd.Series({'ID':24,'Name':'bell','score':109})
students.iloc[23]=stu

# 插入一行,在19,20索引行之间
#  首先还是创建一个新序列
stu =pd.Series({'ID':101,'Name':'Danni','score':100})
part1 = students[:20]  #切到19,不到20
part2 = students[20:]  #从20,切到底
students=part1.append(stu,ignore_index=True).append(part2).reset_index(drop='True')

# 删除行
# students.drop(index=[0,1,2],inplace=True)
#students.drop(index=range(0,10),inplace=True)

# 用切片删除
# students.drop(index=students[0:10].index,inplace=True)

# 演示删除空行
for i in range(5,15):
	students['Name'].at[i]=''


print(students)
print('@'*50)

missing = students.loc[students['Name']=='']
students.drop(index=missing.index,inplace=True)

print(students)