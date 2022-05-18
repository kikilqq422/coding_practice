# 先要安装几个库 sqlalchemy, pandas,mysql-connector
from sqlalchemy import create_engine
import pandas as pd
import os
import datetime
import pymysql
pymysql.install_as_MySQLdb()

starttime = datetime.datetime.now()

# 定义路径
path = '/Users/qiqili/Desktop/MySQL video/pandas/mysql/导入那Navicate/'
# 首先打开文件
files = os.listdir(path)
for i in files:
    if '.xlsx' in i:
        path1 = path + i
        data = pd.read_excel(path1)
        # 自动生成filename
        filename = '' + i
        engine = create_engine('mysql+pymysql://root:kikilqq422@localhost:3306/deli_prac?charset=utf8',encoding = 'utf-8')
        data.to_sql(name=filename, con=engine.connect(),if_exists="append",index=False,chunksize=100)

        print('导入' + filename + '成功')
        endtime = datetime.datetime.now()
        x = endtime - starttime
        print(x.seconds)
'''
导入到mysql，这里有几个关键点，name是Table的名称，if_exists是指Table如果存在的几
个处理办法，默认是报错，replace是先删后写入，append是添加，chunksize很关键，如
果数据量较大，可以分批写入，chunksize后的数字就是每次写入的行数，可以加快运行速
度，而且如果Table不存在，语句能自动创建，还能根据源数据自动调整Table字段的属
性，效果很好
'''
