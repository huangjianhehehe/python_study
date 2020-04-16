#coding=utf-8

import os
import sys

import pandas as pd

file1 ='E:\python_study\python_xls\0416\20200414.csv'
file2 = 'E:\python_study\python_xls\0416\20200415.csv'
file3 ='E:\python_study\python_xls\0416\20200416.csv'
file4= 'E:\python_study\python_xls\0416\20200416_b.csv'
file5 = 'E:\python_study\python_xls\0416\20200416_c.csv'
file6= 'E:\python_study\python_xls\0416\20200416_new.csv'

file = [file1,file2,file3,file4,file5,file6]
li = []
for i in file:
	li.append(pd.read_csv(i))

print(li)