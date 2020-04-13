import  pandas as pd
import  matplotlib.pyplot as plt

students=pd.read_excel('e:/python_xls/students.xlsx')

# 2017列排序，直接产生效果
students.sort_values(by='2017',inplace=True,ascending=False)

print(students)

# 分组柱状图设置
students.plot.bar(x='Field',y=['2016','2017'],color=['orange','red'])

plt.title('International Students by Field',fontsize=16,fontweight='bold')

plt.xlabel('Field',fontweight='bold')
ax = plt.gca()
ax.set_xticklabels(students['Field'],rotation=45,ha='right') # 水平右对齐
f=plt.gcf()
f.subplots_adjust(left=0.2,bottom=0.42)
plt.tight_layout()

plt.show()

