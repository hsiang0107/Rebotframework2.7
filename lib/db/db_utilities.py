import pyodbc, string
from lib.ConfigHelper import ConfigHelper

drv = pyodbc.drivers()
# print(drv)


def make_connection():
    config = ConfigHelper()
    sqlserver = config.get_data_from_config('DB', 'address')
    dbname = config.get_data_from_config('DB', 'dbname')
    username = config.get_data_from_config('DB', 'account')
    password = config.get_data_from_config('DB', 'password')
    sep = ';'
    conn_string = sep.join(('DRIVER={SQL Server}', 'SERVER=' + sqlserver,
                            'DATABASE=' + dbname, 'UID=' + username,
                            'PWD=' + password))
    cxn = pyodbc.connect(conn_string)
    return cxn


def exec_select(cur, sql):
    cur.execute(sql)
    return cur


def exec_sql_file(cur, file):
    sql_query = ''
    with open(file, 'r') as script:
        sql = script.readlines()
        for line in sql:
            if line == 'GO\n' or line == 'GO':
                cur.execute(sql_query)
                sql_query = ''
            else:
                sql_query = sql_query + line

    cur.commit()
    return cur
