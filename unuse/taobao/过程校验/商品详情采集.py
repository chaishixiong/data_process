import pymysql
import re
import time
def connect_sql(sql):
    host = "192.168.0.228"
    port = 3306
    db = "e_commerce"
    name = "dev"
    password = "Data227or8Dev715#"
    connect1 = pymysql.connect(host=host, port=port, db=db, user=name, passwd=password, charset="utf8",
                               use_unicode=True, cursorclass=pymysql.cursors.Cursor)
    cursor = connect1.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connect1.close()
    return data

def tongji(sql,num,platform,w_file):

    data_s = connect_sql(sql)
    data =[float(i[0]) for i in data_s]
    totle_sale_count = len(data)
    totle_sale_money = sum(data)
    w_file.write(platform+str(num)+"有效店铺数量："+str(totle_sale_count)+"\n")
    w_file.write(platform+str(num)+"总销售额数量："+str(totle_sale_money)+"\n")
    w_file.flush()
    print(totle_sale_count)
    print(totle_sale_money)

if __name__ == "__main__":
    path = r"X:/数据库/taobaotmall/过程校验/商品详情/"
    platform = "taobao"
    w_file = path + "{}销量统计结果.txt".format(platform)
    w_file = open(w_file, "a+", encoding="utf-8")
    show_tables = '''show tables'''
    tables = connect_sql(show_tables)
    for i in tables:
        match = re.search("(platform)_shopinfo_(\d{6})$".replace("platform",platform),i[0])
        if match:
            platform = match.group(1)
            num = match.group(2)
            if int(num)>201808:
                print(platform)
                print(num)
                sql = '''select sales_money from {}_shopinfo_{} where sales_money > 0'''.format(platform,num)
                try:
                    time_first = time.time()
                    tongji(sql,num,platform,w_file)
                    time_last = time.time()
                    print(time_last-time_first)
                except Exception as e:
                    print(e)