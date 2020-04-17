import  pandas as pd
import  numpy as np

page_001 = pd.read_excel(r'./Students_Score.xlsx',sheet_name='Page_001')

page_002 = pd.read_excel(r'./Students_Score.xlsx',sheet_name='Page_002')

# 把两张表竖向拼接
students = pd.concat([page_001,page_002],axis=0).reset_index(drop=True)

# 把两张表横向拼接
# students = pd.concat([page_001,page_002],axis=1).reset_index(drop=True)

# 追加一列
students['Age']=np.arange(0,len(students))

# 删除列
students.drop(columns=['Age','score'],inplace=True)

# 插入一列
students.insert(2,column='Foo',value=np.repeat('foo',len(students)))

# 重命名列
students.rename(columns={'Foo':'FOO','Name':'NAME'},inplace=True)

# 转浮点数
students['ID'] =students['ID'].astype(float)

# 批量设置列数值
for i in range(5,15):
	students['ID'].at[i]=np.nan

# 删除NaN
students.dropna(inplace=True)
print(students)