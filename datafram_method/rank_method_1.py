# _*_coding:utf-8 _*_
# @Time　　 :2021/6/25/025   14:24
# @Author　 : Antipa
# @File　　 :rank_method_1.py
# @Theme    :排序编号以及分组排序编号，topN 的行
import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)


df=pd.DataFrame({'grade':['a','a','a','b','b','a','a','b','a','b'],
                 'name':['n1','n2','n3','n4','n5','n6','n7','n8','n9','n10'],
                 'gender':['f','m','m','f','f','m','f','m','m','m'],
                 'height':[170,167,155,167,166,177,189,146,168,177]
                 })
# 相同值则取rank中间值
df['height_rank_ave']=df.height.rank(axis=0,method='average',ascending=True)

# 相同值则取rank不并列
df['height_rank_fir']=df.height.rank(axis=0,method='first',ascending=True)

# 相同值则取rank并列
df['height_rank_den']=df.height.rank(axis=0,method='dense',ascending=True)

# 分组排序
df.sort_index(axis=0,by=['grade','gender'],ascending=[False,True],inplace=True)
df['group_then_height_rank']=df.groupby(['grade','gender'])['height'].rank(method='first')

df['group_then_height_rank']=df.groupby(['grade','gender'])['height'].rank(method='first')
df.nlargest(2,'group_then_height_rank')

# 取topN
df.nlargest(2,'height',keep='all')
df.nlargest(2,'height',keep='first')
df.nlargest(2,'height',keep='last')

# 取lastN
df.nsmallest(2,'height',keep='all')