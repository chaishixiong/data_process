# -*- coding: utf-8 -*-
import os
from pathlib import Path
import time
import pymysql


path = "/data/mysql"
db_name = ["2017double11_tb","ec_cross_border","life_server","oridata","oridata_1688","oridata_ec_other","oridata_jd","oridata_taobao","oridata_tmall"]
backup_path = "/data/backup_hz/online_upload/"
table_key_name = "online_data"
table_error_name = "online_error"

sql_prame = {
    "host": "192.168.0.227",
    "db": "oridata_backup",
    "user": "update",
    "password": "change227NRIAT!#$",
    "port" : 9227
}
blacklist = []
with open("/data/python_project/safe_backup/blacklist.txt","r",encoding="utf-8") as f:
    for i in f:
        blacklist.append(i.strip())
whitelist = []
with open("/data/python_project/safe_backup/whitelist.txt","r",encoding="utf-8") as f:
    for i in f:
        whitelist.append(i.strip())

whitelist_MYD = [i+".MYD" for i in whitelist]
blacklist_MYD = [i+".MYD" for i in blacklist]

def msyql_compression(db_name,table_name,table_time):
    frm_name = "{}.frm".format(table_name)
    myd_name = "{}.MYD".format(table_name)
    myi_name = "{}.MYI".format(table_name)
    compression = "{}#spilit#{}#spilit#{}.7z".format(db_name, table_name, table_time)
    cps_file = "{}/{}".format(backup_path,compression)
    return zip7(cps_file,[frm_name,myd_name,myi_name])


def zip7(cps_file,files_name):#
    try:
        print("正在压缩", cps_file)
        cmd = "7za a {} {}".format(cps_file," ".join(files_name))
        # cmd = "7z a {} {}".format(cps_file," ".join(files_name))
        a = os.popen(cmd)
        console_str = a.read()
        if "Ok" in console_str:
            print("ok")
            return 1
        else:
            return 0
    except Exception as e:
        return 0


def get_table(db_nanme,days):#5.7mysql数据文件下的数据库
    blacklist_MYD_db = []
    for i in blacklist_MYD:
        if i.split("#spilit#")[0] == db_name:
            try:
                blacklist_MYD_db.append(i.split("#spilit#")[1])
            except Exception as e:
                print(e)
    db_path = Path(path)/db_nanme
    tables = os.listdir(db_path)
    for table in tables:
        if ".MYD" in table:
            if whitelist:
                if table in whitelist_MYD:
                    statinfo = os.stat(db_path/table)
                    table_time = statinfo.st_mtime
                    table_name = str(table).replace(".MYD","")
                    print(table_name,str(int(table_time)))
                    yield (table_name,str(int(table_time)))
            else:
                statinfo = os.stat(db_path/table)
                table_time = statinfo.st_mtime
                if table_time > time.time()-3600*24*days and table not in blacklist_MYD_db:
                    table_name = str(table).replace(".MYD", "")
                    print(table_name,str(int(table_time)))
                    yield (table_name,str(int(table_time)))

def run(db_name,days):
    db_path = Path(path)/db_name
    os.chdir(db_path)#修改为7-Zip目录
    sql_class = table_key_sql(sql_prame)
    for i in get_table(db_name,days):
        table_name = i[0]
        table_time = i[1]
        if os.path.exists(table_name+".frm") and os.path.exists(table_name+".MYI"):
            table_key = "{}#spilit#{}#spilit#{}".format(db_name,table_name,table_time)
            judge_result = sql_class.judge_key(table_key,table_key_name)
            if judge_result:
                result = msyql_compression(db_name,table_name,table_time)
                if not result:
                    sql_class.del_key(table_key,table_key_name)
                    sql_class.judge_key(table_key+str(int(time.time())),table_error_name)

class table_key_sql:
    def __init__(self,sql_prame):
        '''CREATE TABLE `online_data` (
  `table_key` varchar(255) NOT NULL COMMENT '已完成备份的key集合',
  PRIMARY KEY (`table_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
        '''
        self.connect = pymysql.connect(host=sql_prame.get("host"), port=sql_prame.get("port", 3306), db=sql_prame.get("db"),
                                  user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                                  use_unicode=True, cursorclass=pymysql.cursors.Cursor)
        self.cursor = self.connect.cursor()

    def judge_key(self,key,table_key_name):
        sql = 'insert into {} value ("{}")'.format(table_key_name,key)
        try:
            self.cursor.execute(sql)
            return 1
        except pymysql.err.IntegrityError:
            return 0

    def del_key(self,key,table_key_name):
        sql = 'DELETE from {} where table_key = "{}"'.format(table_key_name,key)
        result = self.cursor.execute(sql)
        return result

    def del_key_like(self,key,table_key_name):
        sql = 'DELETE from {} where table_key like "%%{}%%"'.format(table_key_name,key)
        result = self.cursor.execute(sql)
        return result

    def get_data(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def clear_error(self):
        online_error = self.get_data("select table_key from online_error")
        error_table = {i[0][:-10] for i in online_error}
        online_table = {i[0] for i in self.get_data("select table_key from online_data")}
        online_delete = error_table & online_table
        for i in online_delete:
            self.del_key_like(i,table_error_name)


    def __del__(self):
        self.cursor.close()
        self.connect.close()



if __name__ == "__main__":
    for i in db_name:
        run(i, 30)
    else:
        sql_class = table_key_sql(sql_prame)
        sql_class.clear_error()
# a = table_key_sql(sql_prame)
# a.judge_key("tmall_shop_infs-1541541")
# a.del_key("tmall_shop_infs-1541541")