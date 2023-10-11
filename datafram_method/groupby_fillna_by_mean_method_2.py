# _*_coding:utf-8 _*_
# @Time　　 :2021/6/23/023   15:34
# @Author　 : Antipa
# @File　　 :groupby_fillna_by_mean_method_2.py
# @Theme    :0值用nna填充，数据分组求平均值并填充nan

# df.val_col_1 & df[val_col_1]返回的数据类型是pandas.Series,df.loc[:,[val_col_1]返回数据类型 pandas,DataFrame,df.loc[:,val_col_1]返回数据类型是 pandas.Series
# df.groupby返回数据类型是pandas.DataFrame

import pandas as pd
import numpy as np
import os

file_path=os.path.join(os.getcwd(),'hive_liuan_tool_matrix_mau_dau_zhuangji.csv')

df_matrix=pd.read_csv(file_path)

df_part_matrix=df_matrix[df_matrix.qiye.isin(['北京好达','北京那湾'])]
print(df_part_matrix)

# 数值指标字段
value_val_columns=['zhuangji_cnt','sum_dau']

for val_col in value_val_columns:
    index_equel_zero=df_part_matrix[val_col]==0
    df_part_matrix.loc[index_equel_zero,val_col]=np.nan

# 分类字段
groupby_val_column_list=['qiye']
df_part_matrix_mean=df_part_matrix.groupby(groupby_val_column_list)[value_val_columns].mean()

for val_col in value_val_columns:
    # val_col val_columns
    for qiye_name in df_part_matrix_mean.index:
        # groupby_column_list 分组变量
        # series_tmp返回的数据类型是pandas.Series，因为loc参数不全是列表
        series_tmp=df_part_matrix.loc[df_part_matrix[groupby_val_column_list[0]]==qiye_name,val_col]
        where_=np.where(np.isnan(series_tmp))[0]
        # if not where_.any():
        #     continue
        index_equal_nan=series_tmp.index[where_]

        print('index_equal_nan:',index_equal_nan)
        print(df_part_matrix.loc[index_equal_nan,val_col])
        df_part_matrix.loc[index_equal_nan,val_col]=df_part_matrix_mean.loc[qiye_name,val_col]
print(df_part_matrix)