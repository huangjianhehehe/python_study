import  pandas as pd
import pyodbc
import  sqlalchemy

# 连接mssql方法
engine =sqlalchemy.create_engine('mssql+pyodbc://sa:1234@192.168.101.128/studentdb?driver=SQL+Server')


query = "select * from 员工信息 "

df1 = pd.read_sql_query(query,engine)

print(df1.head())