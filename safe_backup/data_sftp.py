#!/usr/bin/python
# coding=utf-8
import paramiko
import os
import time
import pymysql
from dingding import run as ding_run
# def sftp_upload(host,port,username,password,local,remote):
#     sf = paramiko.Transport((host,port))
#     sf.connect(username = username,password = password)
#     sftp = paramiko.SFTPClient.from_transport(sf)
#     try:
#         if os.path.isdir(local):#判断本地参数是目录还是文件
#             for f in os.listdir(local):#遍历本地目录
#                 sftp.put(os.path.join(local+f),os.path.join(remote+f))#上传目录中的文件
#         else:
#             sftp.put(local,remote)#上传文件
#     except Exception,e:
#         print('upload exception:',e)
#     sf.close()
class sftp_data():
    def __init__(self,host,port,username,password):
        self.sf = paramiko.Transport((host, port))
        self.sf.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.sf)

    def sftp_download(self,local,remote):
        remote_list = self.sftp.listdir(remote)
        num = len(remote_list)
        num_success = 0
        for f in remote_list:#遍历远程目录
            remote_file = remote + "/" + f
            local_file = os.path.join(local,f)
            if not os.path.exists(local_file):
                try:
                    self.sftp.get(remote_file,local_file)#下载目录中文件
                    num_success += 1
                except Exception as e:
                    print(remote_file+"下载失败")
                    os.remove(local_file)
                else:
                    self.sftp.remove(remote_file)
        return (num,num_success)

    def __del__(self):
        self.sf.close()
def ding_online(new_table,loads_success_table,online_error_table):
    request_text = '''电商数据周备份:
    新增备份数量:{}
    下载成功数量:{}
    压缩错误数量:{}
    '''.format(new_table,loads_success_table,online_error_table)
    ding_run(request_text)

if __name__ == '__main__':
    port = 22 #端口
    username = 'root' #用户名
    local = "/home/gmsz/backup_hz/online_loads"#本地文件或目录，与远程一致，当前为windows目录格式，window目录中间需要使用双斜线
    remote = "/data/backup_hz/online_upload"#远程文件或目录，与本地一致，当前为linux目录格式
    host_list = [('192.168.0.228','Nriat&Y8903a'),('192.168.0.227',"NRIAT227d!a@t#a$")]
    table_num = 0
    table_success = 0
    for i in host_list:
        host = i[0]
        password = i[1]
        sftp = sftp_data(host,port,username,password)
        num,num_success = sftp.sftp_download(local,remote)#下载
        num_success1 = 0
        if num_success < num:
            time.sleep(600)
            sftp = sftp_data(host, port, username, password)
            num1, num_success1 = sftp.sftp_download(local, remote)
        table_num +=num
        table_success += num_success+num_success1
    sql_prame = {
        "host": "127.0.0.1",
        "db": "oridata_backup",
        "user": "root",
        "password": "hzAllroot"
    }
    connect = pymysql.connect(host=sql_prame.get("host"), port=sql_prame.get("port",3306), db=sql_prame.get("db"),
                               user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                               use_unicode=True, cursorclass=pymysql.cursors.Cursor)
    cursor = connect.cursor()
    print("INSERT into loadsfile VALUES ({},{},CURRENT_TIME);".format(table_num,table_success))
    sql = "INSERT into loadsfile VALUES ({},{},CURRENT_TIME);".format(table_num,table_success)
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()

    sql_prame = {
        "host": "192.168.0.227",
        "db": "oridata_backup",
        "user": "read",
        "password": "nriat227read@x#",
        "port":9227
    }
    try:
        connect = pymysql.connect(host=sql_prame.get("host"), port=sql_prame.get("port",3306), db=sql_prame.get("db"),
                                   user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                                   use_unicode=True, cursorclass=pymysql.cursors.Cursor)
        cursor = connect.cursor()
        sql = "select count(1) from online_error;"
        cursor.execute(sql)
        online_error = cursor.fetchone()[0]
        if online_error != 0:
            online_error = "{}:见227oridata online_error"
    except:
        online_error = "227数据库连接错误"
    ding_online(table_num,table_success,online_error)
    cursor.close()
    connect.close()
