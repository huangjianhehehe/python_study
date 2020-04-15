import  pandas as pd

people = pd.read_excel('./People_all.xlsx',index_col='ID')

df = people['Full Name'].str.split(expand=True) #expand直接生成两列

people['First Name']=df[0].str.lower() # 通过str方法大小写等
people['Last Name']=df[1].str.upper()


people.to_excel('./People_all.xlsx',sheet_name='分开表')