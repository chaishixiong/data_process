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
    print(num)
    headers = cursor.description
    data = cursor.fetchall()#匹配表里的data
    return data,num,headers
connect1 = pymysql.connect(host=host,port=port,db=db2,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
# sql_select = '''select sum(reviews),sum(reviews*(price_now+price_lod)/2),seller_id from lazadacoid_goodsinfo_201909 group by seller_id limit 10;'''
sql_select = '''SELECT reviews,shop_id from amazonus_goodsinfo_201908
where reviews != "" and reviews is not null
'''

data,num,headers = get_data(connect1,sql_select)
connect1.close()
data_dict = defaultdict(list)

sql_update = '''UPDATE amazonus_shopinfo_201908 set transactions_j = "{}" where shop_id = "{}"'''
connect_up = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
cursor_up = connect_up.cursor()
print_num = 0
for one_data in data:
    if print_num%10000 == 0:
        print(print_num)
    print_num += 1
    try:
        sales_num = one_data[0]
        shop_id = one_data[1]
        sales_num = sales_num.replace("，","")
        data_dict[shop_id].append((int(sales_num)))
    except Exception as e:
        print(e)
num_a = 0
for i,y in data_dict.items():
    seller_id = i
    transactions = str(sum([j for j in y]))


    if transactions and transactions != "0":
        sql_test = sql_update.format(transactions,seller_id)
        print(num_a)
        num_a += 1
        try:
            cursor_up.execute(sql_test)
        except Exception as e:
            print(e)
cursor_up.close()
connect_up.close()