#coding=utf8
import datetime
#import logging
import logging.config
import os
import sys
import pandas as pd
import numpy as np


li = list()

files = os.listdir()
for f in files:
	if f.endswith('.csv'):
		li.append(pd.read_excel(f))
writer = pd.ExcelWriter(r'.\union.xlsx')
pd.concat(li).to_excel(writer,'Sheet1',index=False)
writer.save()



