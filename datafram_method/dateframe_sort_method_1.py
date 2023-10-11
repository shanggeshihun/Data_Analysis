# _*_coding:utf-8 _*_
# @Time　　 :2021/6/24/024   14:26
# @Author　 : Antipa
# @File　　 :dateframe_sort_method_1.py
# @Theme    :PyCharm

import pandas as pd
import numpy as np
import os

file_path=os.path.join(os.getcwd(),'hive_liuan_tool_matrix_mau_dau_zhuangji.csv')

df_matrix=pd.read_csv(file_path)

df_part_matrix=df_matrix[df_matrix.qiye.isin(['北京好达','北京那湾'])].loc[:,['qiye','package_name','4_mau','3_mau']]

a=df_part_matrix.sort_index(axis=0,ascending=False,by=['qiye','4_mau'])
b=df_part_matrix.sort_index(axis=0,by=['qiye','3_mau'],ascending=[False,False])
print(b)