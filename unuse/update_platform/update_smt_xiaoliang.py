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
    cursor.execute(sql_select)

    # data = cursor.fetchall()#匹配表里的data
    num = 0
    while True:
        num+=1
        if num%100000==1:
            print(num)
        data = cursor.fetchone()
        if not data:
            break
        yield data
connect1 = pymysql.connect(host=host,port=port,db=db2,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.SSCursor)
sql_select = '''SELECT minPrice,maxPrice,sales_num,shop_id from smt_goodsinfo_201910 
where sales_num != "" and sales_num is not null and sales_num !="0"
'''

# data = get_data(connect1,sql_select)
# connect1.close()
data_dict = defaultdict(list)

print_num = 0
cursor = connect1.cursor()
cursor.execute(sql_select)

# data = cursor.fetchall()#匹配表里的data

while True:
    one_data = cursor.fetchone()
    if not one_data:
        break
    if print_num%10000 == 0:
        print(print_num)
    print_num += 1

    try:
        minPrice = one_data[0]
        maxPrice = one_data[1]
        sales_num = one_data[2]
        shop_id = one_data[3]

        dian_num = minPrice.count(".")

        if dian_num > 1:
            minPrice = minPrice.replace(".", "", dian_num - 1)
        dian1_num = maxPrice.count(".")
        if dian1_num > 1:
            maxPrice = maxPrice.replace(".", "", dian1_num - 1)

        if minPrice:
            minPrice = minPrice.replace("，", "")

            if maxPrice and maxPrice != "0":
                maxPrice = maxPrice.replace("，", "")

                data_dict[shop_id].append((int(sales_num),int(sales_num)*(float(minPrice)+float(maxPrice))/2))
            else:
                data_dict[shop_id].append((int(sales_num), int(sales_num) * float(minPrice)))
        else:
            data_dict[shop_id].append((int(sales_num), 0))

    except Exception as e:
        print(e)
num_a = 0

# sql_update = '''UPDATE smt_shopinfo_201910_com  set transactions_j = "{}",sales_volume_j = "{}" where shop_id = "{}"'''
# connect_up = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
# cursor_up = connect_up.cursor()
with open("D:\data_process\smt10\{smt_shopsale}[shop_id,transactions,sales_volume]","w",encoding="utf-8") as f:
    for i,y in data_dict.items():
        seller_id = i
        transactions = str(sum([j[0]for j in y]))
        sales_volume = str(round(sum([j[1]for j in y])))

        if transactions and transactions != "0":
            sql_test = ",".join([seller_id,transactions,sales_volume])
            if num_a%10000==1:
                print(num_a)
                f.flush()
            num_a += 1
            try:
                # cursor_up.execute(sql_test)
                f.write(sql_test+"\n")
            except Exception as e:
                print(e)
# cursor_up.close()
# connect_up.close()