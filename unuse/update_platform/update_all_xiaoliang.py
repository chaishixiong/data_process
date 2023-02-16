#匹配各个表入库
import pymysql
from collections import defaultdict

host = "192.168.0.227"
port = 3306
db = "ec_cross_company"
name = "dev"
password = "Data227or8Dev715#"

amazon = {"key":"shop_id","key1":"shop_id","table":"amazonus_shopinfo_201908","platform":"亚马逊美国"}
dh = {"key":"shop_id","key1":"shop_id","table":"dhgate_shopinfo_201907","platform":"敦煌"}
alibabagj = {"key":"shop_id","key1":"shop_id","table":"alibabagj_shopinfo_201908","platform":"阿里巴巴国际站"}
dict_p = amazon
def get_data(connect,sql_select):
    cursor = connect.cursor()
    num = cursor.execute(sql_select)
    print(num)
    headers = cursor.description
    data = cursor.fetchall()#匹配表里的data
    return data,num,headers
connect1 = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
sql_select = '''select transactions_j,sales_volume_j,{} from {}
where transactions_j is not null and transactions_j != ""
'''.format(dict_p.get("key"),dict_p.get("table"))

data,num,headers = get_data(connect1,sql_select)
connect1.close()
data_dict = defaultdict(list)

sql_update = '''UPDATE all_shopinfo_company set transactions_j = "{}",sales_volume = "{}" where {} = "{}"and platform ="{}"'''
connect_up = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
cursor_up = connect_up.cursor()
print_num = 0
for one_data in data:
    print(print_num)
    print_num += 1
    try:
        transactions_j = one_data[0]
        sales_volume_j = one_data[1]
        shop_id = one_data[2]
        sql_test = sql_update.format(transactions_j,sales_volume_j,dict_p.get("key1"),shop_id,dict_p.get("platform"))
        cursor_up.execute(sql_test)

    except Exception as e:
        print(e)

cursor_up.close()
connect_up.close()