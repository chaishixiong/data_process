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
sql_select = '''SELECT price_dollar,sales_count,seller_name from ebay_goodsinfo_201907 
where sales_count != "" and sales_count is not null 
'''

data,num,headers = get_data(connect1,sql_select)
connect1.close()
data_dict = defaultdict(list)

sql_update = '''UPDATE ebay_usrinfo_201907 set transactions = "{}",sales_volume = "{}" where seller_name = "{}"'''
connect_up = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
cursor_up = connect_up.cursor()
print_num = 0
for one_data in data:
    if print_num%10000 == 0:
        print(print_num)
    print_num += 1

    try:
        minPrice = one_data[0]
        # maxPrice = one_data[1]
        sales_num = one_data[1]
        shop_id = one_data[2]

        minPrice= minPrice.replace("，","")
        sales_num= sales_num.replace("，","")

        # maxPrice= maxPrice.replace("，","")

        dian_num = minPrice.count(".")
        if dian_num > 1:
            minPrice = minPrice.replace(".", "", dian_num - 1)
        # dian1_num = maxPrice.count(".")
        # if dian1_num > 1:
        #     maxPrice = maxPrice.replace(".", "", dian1_num - 1)

        if minPrice:
            # if maxPrice and maxPrice != "0":
            #     data_dict[shop_id].append((int(sales_num),int(sales_num)*float(minPrice)*float(maxPrice)/2))
            # else:
            data_dict[shop_id].append((int(sales_num), int(sales_num) * float(minPrice)))
        else:
            data_dict[shop_id].append((int(sales_num), 0))

    except Exception as e:
        print(e)
num_a = 0
for i,y in data_dict.items():
    seller_id = i
    transactions = str(sum([j[0]for j in y]))
    sales_volume = str(round(sum([j[1]for j in y])))

    if transactions and transactions != "0":
        sql_test = sql_update.format(transactions,sales_volume,seller_id)
        print(num_a)
        num_a += 1
        try:
            cursor_up.execute(sql_test)
        except Exception as e:
            print(e)
cursor_up.close()
connect_up.close()