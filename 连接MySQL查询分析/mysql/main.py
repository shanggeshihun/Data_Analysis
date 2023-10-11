# _*_coding:utf-8 _*_
# @Time　　 :2021/6/18/018   16:23
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm

from OperatorMysql import MysqlConnect
import os


# 实例化mysql，查询待更新的数据信息
from get_conf import get_mysql_conf, get_es_conf
mysql_conf = get_mysql_conf()
username, password, host_ip, port, database = mysql_conf['user'], mysql_conf['password'], mysql_conf[
    'host'], mysql_conf['port'], mysql_conf['database']

operator_mysql = MysqlConnect(username, password, host_ip, port, database)

with open(os.path.join(os.getcwd(),'dql.sql')) as f:
    sql =f.read()
select_data = operator_mysql.get_data(sql)
print(type(select_data))