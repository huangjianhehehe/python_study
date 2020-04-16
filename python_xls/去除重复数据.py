import  pandas as pd

data = pd.read_excel(r'.\union.xlsx')
data.drop_duplicates(subset=['Frm_SN'],inplace=True,keep='first')
print(type(data))

data.to_excel(r'.\union_new.xlsx','sheet1',index=False)