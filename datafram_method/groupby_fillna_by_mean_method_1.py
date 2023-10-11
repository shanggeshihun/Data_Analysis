# _*_coding:utf-8 _*_
# @Time　　 :2021/6/24/024   10:17
# @Author　 : Antipa
# @File　　 :groupby_fillna_by_mean_method_1.py
# @Theme    :PyCharm
# df.col_1 & df[col_1]返回的数据类型是pandas.Series,df.loc[:,[col_1]返回数据类型 pandas,DataFrame,df.loc[:,col_1]返回数据类型是 pandas.Series
# df.groupby返回数据类型是pandas.DataFrame

import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

file_path=os.path.join(os.getcwd(),'hive_liuan_tool_matrix_mau_dau_zhuangji.csv')

df_matrix=pd.read_csv(file_path)

df_part_matrix=df_matrix[df_matrix.qiye.isin(['北京好达','北京那湾'])]
print(df_part_matrix)

# 数值指标字段
value_columns_list=['zhuangji_cnt','sum_dau']

for col in value_columns_list:
    index_equel_zero=df_part_matrix[col]==0
    df_part_matrix.loc[index_equel_zero,col]=np.nan

# 分类字段
groupby_column_list=['qiye']
groupby_column=groupby_column_list[0]
df_part_matrix_mean=df_part_matrix.groupby(groupby_column_list)[value_columns_list].mean()
print(df_part_matrix_mean)

for val_col in value_columns_list:
    # col columns
    for qiye_name in df_part_matrix_mean.index:
        # groupby_column_list 分组变量
        # df_tmp返回的数据类型是pandas.DataFrame,，因为loc参数是列表
        # 北京那湾的sum_dau的数据
        df_tmp=df_part_matrix.loc[df_part_matrix[groupby_column_list[0]]==qiye_name,[val_col]]
        index_equal_nan=df_tmp.loc[df_tmp[val_col].isna(),:].index
        df_part_matrix.loc[index_equal_nan,[val_col]]=df_part_matrix_mean.loc[qiye_name,val_col]

# 高于组内均值的标记 1
for val_col in value_columns_list:
    flag_column=val_col + '_flag'
    # col columns
    for qiye_name in df_part_matrix_mean.index:
        tmp_mean=df_part_matrix_mean.loc[qiye_name,val_col]
        for_flag_df=(df_part_matrix[groupby_column]==qiye_name) & (df_part_matrix[val_col]>tmp_mean)
        df_part_matrix.loc[for_flag_df,flag_column]=1
    df_part_matrix[flag_column].fillna(0,inplace=True)
print(df_part_matrix)

# 统计每列的统计量
print(df_part_matrix.max(axis=0))
# 统计每行的统计量
print(df_part_matrix.max(axis=1))