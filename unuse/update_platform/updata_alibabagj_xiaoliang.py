#匹配softtime
import pymysql
from collections import defaultdict

host = "192.168.0.227"
port = 3306
db = "ec_cross_company"
db2 = "ec_cross_border"
name = "dev"
password = "Data227or8Dev715#"

def get_data(connect,sql_select):
    cursor = connect.cursor()
    num = cursor.execute(sql_select)
    # print(num)
    headers = cursor.description
    data = cursor.fetchall()#匹配表里的data
    return data,num,headers
# connect1 = pymysql.connect(host=host,port=port,db=db2,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
# sql_select = '''SELECT price,price_low,sales_num,shop_id from alibabagj_goodsinfo_201908
# where sales_num != "" and sales_num is not null'''
#
# data,num,headers = get_data(connect1,sql_select)
# connect1.close()
# data_dict = defaultdict(list)
data_dict = dict()
with open(r"C:\Users\admin\Desktop\阿里巴巴_合并1.txt_去重.txt","r",encoding="UTF-8") as f:
    for i in f:
        data = i.strip().split(",")
        data_dict[data[0]] = data[1]

sql_select = "select DISTINCT index_id,`key` from alibabagj_shopinfo_test"
sql_update = '''UPDATE alibabagj_shopinfo_test set sales_volume_j = "{}" where index_id = "{}"'''
connect_up = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
cursor_up = connect_up.cursor()
print_num = 0
data,num,headers = get_data(connect_up,sql_select)
for one_data in data:
    if print_num%5000 == 0:
        print(print_num)
    print_num += 1
    try:
        key = one_data[1]
        sale = data_dict.get(key)
        if sale:
            sql_test = sql_update.format(sale,one_data[0])
            cursor_up.execute(sql_test)
    except Exception as e:
        print(e)
cursor_up.close()
connect_up.close()