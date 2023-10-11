# _*_coding:utf-8 _*_
# @Time　　 :2021/6/24/024   13:48
# @Author　 : Antipa
# @File　　 :apply_method_1.py
# @Theme    :PyCharm

import pandas as pd
import numpy as np
import os

file_path=os.path.join(os.getcwd(),'hive_liuan_tool_matrix_mau_dau_zhuangji.csv')

df_matrix=pd.read_csv(file_path)

df_part_matrix=df_matrix[df_matrix.qiye.isin(['北京好达','北京那湾'])].loc[:,['qiye','package_name','4_mau','3_mau']]

# 针对每行求统计量
df_part_matrix.max(axis=1)
# 针对每列求统计量
df_part_matrix.max(axis=0)

# 自定义函数求统计量
range_=lambda x:x.max()-x.min()
df_part_matrix['range_row']=df_part_matrix[['4_mau','3_mau']].apply(range_,axis=1)
print(df_part_matrix)

format_unit=lambda x:'%.2f' % x
df_part_matrix[['4_mau','3_mau']].applymap(format_unit)

