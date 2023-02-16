#商务项目
import pymysql
import json
import csv

host = "192.168.0.227"
host_get = "192.168.0.228"
port = 3306
db = "oridata_jd"#数据库要修改
db2 = "ec_cross_border"
db_get = "e_commerce"
name = "dev"
password = "Data227or8Dev715#"
sql_table = '''show tables'''
table_dictkey = "Tables_in_oridata_jd"
need_str = ["jd_goodsinfo_2"]#"amazon_goodsinfo_2","gome_goodsinfo_2","jd_goodsinfo","suning_goodsinfo_2","taobao_goodsmobile","tmall_goodsmobile_2"
sql_selectf = '''select * from {} where shop_id = '{}';'''
sql_insert = '''insert into companygoods_newadd (json_str,from_table) values ('{}','{}')'''#修改tablename
def get_tablenames(connect):
    cursor_table = connect.cursor()
    cursor_table.execute(sql_table)
    a = cursor_table.fetchall()
    need_list = []
    for i in a:
        str = i[table_dictkey]
        for i in need_str:
            if i in str and "copy" not in str:
                if "_" in str:
                    last_str = str.split("_")[-1]
                    if len(last_str) == 6 and (last_str.startswith("2018") or last_str.startswith("2019")):
                        need_list.append(str)
    need_list.remove("jd_goodsinfo_201804")
    cursor_table.close()
    return need_list
def get_iddata(connect,sql_select):
    cursor = connect.cursor()  # select的连接
    cursor.execute(sql_select)
    data = cursor.fetchall()
    return data
def judge_select_insert(connect,connect1,sql_select,table_name):
    cursor = connect.cursor()#select的连接
    cursor.execute(sql_select)
    cursor1 = connect1.cursor()#插入连接
    diaojie = True
    while(diaojie):
        data_one = cursor.fetchone()
        if data_one is None:
            diaojie = False
        else:
            json_str = json.dumps(data_one)
            json_escape = pymysql.escape_string(json_str)
            insert_str = sql_insert.format(json_escape,table_name)
            cursor1.execute(insert_str)
    cursor.close()
    cursor1.close()
connect = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.DictCursor)#商品库
connect_getid = pymysql.connect(host=host_get,port=port,db=db_get,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.DictCursor)#所需要的id
connect1 = pymysql.connect(host=host,port=port,db=db2,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.DictCursor)#存数据的库
need_table = get_tablenames(connect)
sql_select = '''select distinct from_table,shop_id from company_newadd where shop_id is not null;'''
id_datas = get_iddata(connect_getid,sql_select)
for id_data in id_datas:
    from_table = id_data["from_table"]
    shop_id = id_data["shop_id"]
    print("正在处理{}".format(from_table))
    for table_name in need_table:
        if "_" in from_table and "_" in table_name:
            pingtai_1 = from_table.split("_")[0]
            pingtai_2 = table_name.split("_")[0]
            date1 = from_table.split("_")[-1]
            data2 = table_name.split("_")[-1]
            if pingtai_1==pingtai_2 and date1==data2:
                print(id_data)
                print(table_name)
                sql_select = sql_selectf.format(table_name,shop_id)
                judge_select_insert(connect,connect1,sql_select,table_name)
connect.close()
connect1.close()