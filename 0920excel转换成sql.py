# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os
from sas7bdat import SAS7BDAT
import datetime

# 设置程序开始时间
starttime = datetime.datetime.now()

# 设置工作目录
os.chdir(r'D:\Documents\Desktop\...')

# 读取sas文件的数据
with SAS7BDAT('test.sas7bdat',encoding='gb2312') as f:
    mydata_sas = f.to_data_frame()                             # 将数据转换为pandas中的DataFrame格式

# 返回数据框中的数据类型
data_type = []
for i in mydata_sas.columns:
    print(i,type(mydata_sas[i][0]))
    data_type.append(type(mydata_sas[i][0]))      # 合并数据类型
print(set(data_type))                             # 返回数据类型的集合

print(mydata_sas['c_dept_name_rel_achive'].head())

# create table  user_info (user_id int, cid string, ckid string, username string)

"""
数据中的数据类型：
{<class 'str'>    <class 'datetime.date'>    <class 'NoneType'>   <class 'numpy.float64'>}
"""
create_sql = []
for i in mydata_sas.columns:
    print(i,type(mydata_sas[i][0]))                     # 判断每一列的数据类型
    if str(type(mydata_sas[i][0])) == "<class 'datetime.date'>" or str(type(mydata_sas[i][0])) == "<class 'NoneType'>":
        create_sql.append(i + ' ' + 'date')        # 时间类型的数据
    if str(type(mydata_sas[i][0])) == "<class 'str'>":
        create_sql.append(i + ' ' + 'varchar(255)')          # 字符串类型的数据
    if str(type(mydata_sas[i][0])) == "<class 'numpy.float64'>":
        create_sql.append(i + ' ' + 'double')

# 生成创建表的sql语句
with open('create.txt', 'w') as f:
    f.write('create table  user_info(')          # 写入标题行
    for l,k in enumerate(create_sql):
        f.write(''.join(k))          # 写入文本文件
        if l < len(create_sql)-1:
            f.write(',')
        else:
            f.write(')')
        print('写入成功！')

# 生成插入数据的sql语句
with open('insert.txt', 'w') as f:
    for i in range(150000):
        f.write('insert into test1 values(')
        # for l,k in enumerate(mydata_sas.columns):
        #     print(l,k)
        #     f.write(''.join(k))
        #     if l <= 110:
        #         f.write(',')
        #     else:
        #         f.write(')')
        # 写入数据
        for m,n in enumerate(mydata_sas.iloc[i,:]):
            name = mydata_sas.columns[m]
            if str(type(mydata_sas[name][0])) == "<class 'str'>":
                f.write(''.join('"' + str(mydata_sas.iloc[i,m]) + '"'))
            elif str(type(mydata_sas[name][0])) == "<class 'datetime.date'>" or str(type(mydata_sas[name][0])) == "<class 'NoneType'>":
                value = "DATE('" + str(mydata_sas.iloc[i, m]) + "')"     # mysql中时间格式的转换
                f.write(''.join(value))
            else:
                f.write(''.join(str(mydata_sas.iloc[i, m])))
            if m <= 110:
                f.write(',')
            else:
                f.write(')\n')

# 结束时间
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)
