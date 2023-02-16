import pandas
import pymysql
import os
import numpy as np
from pathlib import Path
sql_prame = {
    "host": "192.168.0.227",
    "db": "oridata",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
connect = pymysql.connect(host=sql_prame.get("host"), port=3306, db=sql_prame.get("db"),
                          user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                          use_unicode=True, cursorclass=pymysql.cursors.Cursor)
cursor = connect.cursor()
# ！！！！！！！！！---修改要入库的文件名;上月为结果，新增为 结果_add
path = r"X:\数据库\工商地址库\结果"     #上月数据待入库

# path = r"X:\数据库\工商地址库\结果_add"   #新增数据待入库

# path = r"X:\数据库\工商地址库\亚马逊\结果"     #亚马逊数据待入库

files = os.listdir(path)
for file in files:
    file_path = Path(path)/file
    qichacha_df = pandas.read_excel(file_path,header=1,dtype=str)
    ori_database = 'oridata'
    host_227 = '192.168.0.227'
    keys = 'Data227or8Dev715#'
    user = 'dev'
    engine_str = 'mysql+pymysql://{user}:{pw}@{host}/{db}?charset=utf8'

    # engine_227 = create_engine(engine_str.format(user=user,pw=keys,host=host_227,db=ori_database),encoding='utf-8')
    # qichacha_df.to_sql('company_qichacha_202006',con=engine_227,if_exists='replace',index=False)

    # ！！！！！！！-----在227 新建新月份的表后，company_qichacha_202009 ----修改下面月份
    # sql_str = "insert into company_qichacha_202009  values ('{}')"     #上月数据入库的表

    sql_str = "insert into company_qichacha_09增量  values ('{}')"   #新增数据入库的表
    for i in qichacha_df.values:

        if len(i) == 24:
            data = [pymysql.escape_string(j) if isinstance(j, str) else str(j) for j in i]#字符转义下

            sql = sql_str.format("','".join(data))
            try:
                cursor.execute(sql)
            except Exception as e:
                print(e,sql)
        else:
            i = np.insert(i, 5, '')
            data = [pymysql.escape_string(j) if isinstance(j, str) else str(j) for j in i]  # 字符转义下

            sql = sql_str.format("','".join(data))

            try:
                cursor.execute(sql)
            except Exception as e:
                print(e,sql)

    print(file_path)
