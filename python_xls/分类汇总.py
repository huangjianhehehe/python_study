import pandas as pd
import  numpy as np

data = pd.read_excel(r'.\union_new.xlsx')

# 第一种方式分类汇总
data['Total']='Total' # 新增一列,用于计算总数,index代表行
pt1 = data.pivot_table(index=['Procuct_Id'],columns=['Total'],values='Qty',aggfunc=np.sum) # aggfunc调用 np的函数

# 第二种方式分类汇总
groups = data.groupby(['Procuct_Id'])
s = groups['Qty'].sum()
c = groups['Procuct_Id'].count()
pt2 = pd.DataFrame({'Sum':s,'Count':c})
pt2.to_excel(r'.\ok2.xlsx')



pt1.to_excel(r'.\ok.xlsx')