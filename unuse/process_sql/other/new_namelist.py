#商务桐乡任务
import pymysql
import json
import csv

host = "192.168.0.228"
port = 3306
db = "e_commerce"
name = "dev"
password = "Data227or8Dev715#"
table_dictkey = "Tables_in_e_commerce"
need_str = ["amazon_shopinfo","gome_shopinfo","jd_shopinfo","suning_shopinfo","tmall_shopinfo"]#"amazon_shopinfo","gome_shopinfo","jd_shopinfo","suning_shopinfo","taobao_qiye_shopinfo","tmall_shopinfo"

sql_insert = '''insert into company_newadd (json_str,from_table,shop_id) values ('{}','{}','{}')'''#修改tablename
sql_table = '''show tables'''
mysql_field  = "company"
file_name = "C:/Users/nriat/Desktop/新增名单(1)1 .csv"
file_num = 0

def get_tablenames(connect,sql_table):
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
                    if len(last_str) == 6 and (last_str.startswith("2017") or last_str.startswith("2018") or last_str.startswith("2019")):
                        need_list.append(str)
    cursor_table.close()
    return need_list
def read_csv(file_name,num):
    data = []
    with open(file_name,"r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            data.append(row[num])
    return data
def judge_select_insert(connect,connect1,sql_select,file_data,table_name):
    cursor = connect.cursor()#select的连接
    cursor.execute(sql_select)
    cursor1 = connect1.cursor()#插入连接
    diaojie = True
    while(diaojie):
        data_one = cursor.fetchone()
        if data_one is None:
            diaojie = False
        else:
            if mysql_field in data_one.keys():
                company = data_one[mysql_field]
                if company:
                    company = company.replace("(", "（")
                    company = company.replace(")", "）")
                    for file_company in file_data:
                        file_company = file_company.replace("(", "（")
                        file_company = file_company.replace(")", "）")
                        if (file_company in company) or (company in file_company):#判断下逻辑完善
                            shop_id = data_one.get("shop_id")
                            if shop_id:
                                shop_id = str(shop_id)
                            else:
                                shop_id = "null"
                            json_str = json.dumps(data_one)
                            json_escape = pymysql.escape_string(json_str)
                            insert_str = sql_insert.format(json_escape,table_name,shop_id)
                            cursor1.execute(insert_str)
    cursor.close()
    cursor1.close()

connect = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.SSDictCursor)
connect1 = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.SSDictCursor)
need_table = get_tablenames(connect,sql_table)
sql_selectf = '''select * from {} ;'''#修改 amazon_shopinfo_201803
file_data = read_csv(file_name,file_num)
for i in need_table:
    print("正在处理{}".format(i))
    sql_select = sql_selectf.format(i)
    judge_select_insert(connect,connect1,sql_select,file_data,i)
connect.close()
connect1.close()






