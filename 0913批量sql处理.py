# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import os
import json

# 设置工作目录
os.chdir(r'C:\Users\jk\Desktop')
df = pd.read_excel('test.xlsx') # 读取数据
# print(df.columns)

# create table  user_info (user_id int, cid string, ckid string, username string)
create_sql = []
for i in df.columns:
    # print(type(df[i][0]),df[i][0])          # 判断每一列的数据类型
    if str(type(df[i][0])) == "<class 'numpy.int64'>":
        create_sql.append(i + ' ' + 'int')
    if str(type(df[i][0])) == "<class 'str'>":
        create_sql.append(i + ' ' + 'string')
    if str(type(df[i][0])) == "<class 'pandas.tslib.Timestamp'>":
        create_sql.append(i + ' ' + 'datetime')
    if str(type(df[i][0])) == "<class 'numpy.float64'>":
        create_sql.append(i + ' ' + 'float')

print(tuple(create_sql))
print(len(create_sql))
print('create table  user_info','(',create_sql[0])

# 生成创建表的sql语句
with open('create.txt', 'w') as f:
    f.write('create table  user_info(')          # 写入标题行
    for l,k in enumerate(create_sql):
        f.write(''.join(k))                      # 写入文本文件
        if l < len(create_sql)-1:
            f.write(',')
        else:
            f.write(')')
        print('写入成功！')

# 生成插入数据的sql语句
with open('insert.txt', 'w') as f:
    for i in range(2):
        f.write('insert into mysqltest1 (')
        for l,k in enumerate(df.columns):
            print(l,k)
            f.write(''.join(k))                      # 写入文本文件
            if l < len(create_sql)-1:
                f.write(',')
            else:
                f.write(')')
            # print('写入成功！')
        # 写入数据
        f.write(' value(')
        for m,n in enumerate(df.iloc[i,:]):
            f.write(''.join(str(df.iloc[i,m])))
            if m < len(create_sql)-1:
                f.write(',')
            else:
                f.write(')\n')

print(list(df.iloc[0,:]))
