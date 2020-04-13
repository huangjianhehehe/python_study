# 导入xlrd包
import  xlrd
xls = xlrd.open_workbook('e:/7月.xls')
#打开第一个表
table =xls.sheet_by_index(0)
#可以按名字打开
# table = xls.sheet_by_name("7月")
#以下三种方式都可以获取单元格数据
print(table.cell_value(6,1))
print(table.cell(6,1).value)
print(table.row(6)[1].value)