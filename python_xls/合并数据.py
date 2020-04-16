
import  pandas as pd

file1 = r'.\0416\20200414.csv'
file2 = r'.\0416\20200415.csv'
file3 = r'.\0416\20200416.csv'
file4 = r'.\0416\20200416_new.csv'
files = [file1,file2,file3,file4]
li = list()

# data = csv.reader(open(file1))

for i in files:
	li.append(pd.read_csv(i))

writer = pd.ExcelWriter(r'.\union.xlsx')
pd.concat(li).to_excel(writer,'sheet1',index=False)
writer.save()




