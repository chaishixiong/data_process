import pymysql

db_list = ["2017double11_tb","ec_cross_border","life_server","oridata","oridata_1688","oridata_ec_other","oridata_jd","oridata_taobao","oridata_tmall"]
sql_prame = {
    "host": "192.168.0.227",
    "db": "",
    "user": "read",
    "password": "nriat227read@x#",
    "port":9227
}

with open(r"C:\Users\Administrator\Desktop\227table_result.csv","w",encoding="utf-8") as f:
    for i in db_list:
        db_name = i
        sql_prame["db"] = db_name
        connect = pymysql.connect(host=sql_prame.get("host"), port=sql_prame.get("port",3306), db=sql_prame.get("db"),
                                   user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                                   use_unicode=True, cursorclass=pymysql.cursors.Cursor)
        cursor = connect.cursor()
        cursor.execute("show tables;")
        data = cursor.fetchall()
        for i in data:
            table = i[0]
            try:
                cursor.execute("select count(1) from {}".format(table))
                data1 = cursor.fetchone()
                num = data1[0]
                cursor.execute("select * from {} limit {},1".format(table,num-1))
                data2 = cursor.fetchone()

                status = 1
            except:
                status = 0
            f.write("{},{},{}\n".format(db_name,table,status))
        f.flush()
        cursor.close()
        connect.close()




