import pymysql

def connect_sql(sql):
    host = "192.168.0.228"
    port = 9228
    db = "e_commerce"
    name = "read"
    password = "nriat228SDFSD%@!"
    connect1 = pymysql.connect(host=host, port=port, db=db, user=name, passwd=password, charset="utf8",
                               use_unicode=True, cursorclass=pymysql.cursors.Cursor)
    cursor = connect1.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connect1.close()
    return data
month = int(input("202012(除了1月1月要改):"))
last_month = month-1#这里修改
shop_id_set = set()
#淘宝
sql = '''SELECT shop_id,seller_id from taobao_shopinfo_{}
where province = "浙江"'''.format(last_month)
print(sql)
data = connect_sql(sql)
file = r"X:\数据库\taobao\{taobao_shopid_zhejiang}[shop_id,seller_id].txt"
print(file)
with open(file,"a+",encoding="utf-8") as f:
    for j in data:
        if j[0] not in shop_id_set:
            f.write(",".join(j)+"\n")
            shop_id_set.add(j[0])
#天猫
sql = '''SELECT shop_id,seller_id from tmall_shopinfo_{}
where province = "浙江省"'''.format(last_month)
#     sql = '''SELECT distinct shop_id,seller_id from tmall_shopinfo_{}'''.format(i)
print(sql)
data = connect_sql(sql)
file = r"X:\数据库\taobao\{tmall_shopid_zhejiang}[shop_id,seller_id].txt"
print(file)
with open(file,"a+",encoding="utf-8") as f:
    for j in data:
        if j[0] not in shop_id_set:
            f.write(",".join(j)+"\n")
            shop_id_set.add(j[0])