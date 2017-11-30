# -*- coding: utf-8 -*-
import pandas as pd
import os
os.chdir('C:/Users/jk/Desktop/新建文件夹')
# 定义函数读取数据
def read_file_data(x,y):
    df_1 = pd.DataFrame()       # 构建空的数据集用于合并
    df_2 = pd.DataFrame()       # 构建空的数据集用于合并
    os.chdir(x)                 # 改变工作目录
    for i in os.listdir(x):
        if os.path.isfile(i):
            mydata_1 = pd.read_excel(i)   # 依次读取数据
            mydata_1['lag_1'] = [os.path.splitext(i)[0]] * len(mydata_1)  # 生成一列
            mydata_1['lag_2'] = [y] * len(mydata_1)  # 生成一列
            df_1 = df_1.append(mydata_1)  # 数据合并
        else:
            file = "./" + i
            for j in os.listdir(file):
                filename = file + '/' + j
                mydata_2 = pd.read_excel(filename)  # 依次读取数据
                mydata_2['lag_1'] = [os.path.splitext(j)[0]] * len(mydata_2)  # 生成一列
                mydata_2['lag_2'] = [y] * len(mydata_2)  # 生成一列
                df_2 = df_2.append(mydata_2)  # 数据合并
    result = df_1.append(df_2)
    return result

merge_all = pd.DataFrame()
for i in os.listdir():
    name = i
    path = os.path.join('C:/Users/jk/Desktop/新建文件夹/',i)
    # print(path)
    result_1 = read_file_data(path,name)
    merge_all = merge_all.append(result_1)
print(merge_all)
# 输出数据
os.chdir('C:/Users/jk/Desktop/新建文件夹')
merge_all.to_csv('result.csv')
