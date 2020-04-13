import  pandas as pd

products = pd.read_excel('E:/python_xls/List.xlsx',index_col='ID')

# products.sort_values(by='Price',inplace=True,ascending=False)  #在当前中生成,降序排列

#先按Worthy升序,再按Price降序
products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])

print(products)
