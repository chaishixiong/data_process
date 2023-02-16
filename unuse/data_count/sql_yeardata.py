import pymysql
from collections import defaultdict

host = "192.168.0.228"
port = 3306
db = "e_commerce"
name = "dev"
password = "Data227or8Dev715#"

connect = pymysql.connect(host=host, port=port, db=db, user=name, passwd=password, charset="utf8", use_unicode=True)
cursor = connect.cursor()
table = "a1688_shopinfo_{}"
# sql = '''select shop_id,province from {}#除了1688
# where sales_money>0'''.format(table)
sql = '''select seller_id_en,company_area from {} where month_sales_month>0'''.format(table)#1688
dict_data = defaultdict(list)
shop_set = set()
shop_zhejiang = set()
# shop_list =[]
for i in [202001]:

    sql_str = sql.format(i)
    cursor.execute(sql_str)
    data = cursor.fetchall()
    for j in data:
        # if j[3]:
        #     dict_data[j[0]].append(float(j[3]))
        # if j[0] not in shop_set:
        #     shop_list.append(j)
        shop_set.add(j[0])
        if j[1] and "浙江" in j[1]:
            shop_zhejiang.add(j[0])
print(len(shop_set))
print(len(shop_zhejiang))

# file=open(r"C:\Users\Administrator\Desktop\shopidjd.txt","w",encoding="utf-8")
# for i in shop_list:
#     shopid = i[0]
#     sales_monsy = dict_data.get(shopid)
#     if sales_monsy:
#         totle_money = sum(sales_monsy)
#         if totle_money>5000000:
#             list_data = list(i)
#             list_data[3] = str(totle_money)
#             try:
#                 file.write(",".join(list_data)+"\n")
#             except:
#                 print(1)






