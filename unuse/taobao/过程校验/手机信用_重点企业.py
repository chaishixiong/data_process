import pymysql
from collections import defaultdict
import re
import os

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

def add_data(data_set, platform, num_limit, dizhi_ziduan,mouth,sellernum_limit):#重点企业添加数据规则
    sale_bili = 0.3
    sql = '''select seller_id,{},sales_money from {}_shopinfo_{}
    where province like "%浙江%" and sales_money>0
    order by ABS(sales_money) DESC
    '''.format(dizhi_ziduan, platform,mouth)
    data_sql = connect_sql(sql)
    sale_dict = defaultdict(list)#预留的区域信息
    sale_totle_dict = defaultdict(float)

    num = 1
    for data in data_sql:#数据库取出的原始数据
        if num <= num_limit:
                data_set.add((data[1],data[0],data[2]))#set加入省前一定数量的sellerid
        num += 1
        sale_dict[data[1]].append((data[0],data[2]))#1:地区 0：seller_id 2:销售额
        sale_totle_dict[data[1]] += float(data[2])
    for sale_i in sale_dict:#各地区遍历
        add_sale = 0
        limit_sale = sale_bili * sale_totle_dict[sale_i]
        num1 = 1
        for j in sale_dict[sale_i]:#一个地区的seller遍历
            add_sale += float(j[1])#销售额
            data_set.add((sale_i,j[0],j[1]))#
            if add_sale > limit_sale and num1 > sellernum_limit:
                break
            num1 += 1

def write_file():#将添加的set写入文件中
    platform = "tmall"
    num_limit = 300 #取出的个数
    dizhi = "county"
    platform_1 = "taobao"
    num_limit_1 = 1000
    dizhi_1 = "city"
    mouth = "201910"
    data_set = set()

    add_data(data_set, platform, num_limit, dizhi,mouth,10)#天猫
    add_data(data_set, platform_1, num_limit_1, dizhi_1,mouth,5)#淘宝

    path = r"W:/徐超/淘宝天猫检测/过程校验/手机店铺信用/重点/"
    w_file_more = path + "seller_id_more.txt"
    w_file = path + "seller_id.txt"

    with open(w_file_more, "a+", encoding="utf-8") as f:
        for i in data_set:
            data_str = ",".join(i)
            f.write(data_str + "\n")
    with open(w_file, "a+", encoding="utf-8") as f:#只保留seller_id
        for i in data_set:
            f.write(i[1]+ "\n")

def show_all():#将数据库中筛选出有
    platform_m = "tmall|taobao"
    show_tables = '''show tables'''
    tables = connect_sql(show_tables)
    name_dict =defaultdict(list)
    for i in tables:
        match = re.search("(platform)_shopinfo_(201\d{3})$".replace("platform", platform_m), i[0])
        if match:
            platform = match.group(1)
            num = match.group(2)
            if int(num) > 201808:
                name_dict[num].append(platform)
    return name_dict

def seller_all():
    name_dict = show_all()
    for mouth in name_dict:
        data_set = set()
        for platform in name_dict[mouth]:
            sql = "select seller_id from {}_shopinfo_{} limit 100".format(platform,mouth)
            for seller_data in connect_sql(sql):
                data_set.add(seller_data)
        path = r"Z:/采集数据备份/xc/淘宝天猫检测/过程校验/手机店铺信用/"+str(mouth)
        os.mkdir(path)
        w_file = path+"seller_id.txt"
        with open(w_file, "a+", encoding="utf-8") as f:
            for i in data_set:
                f.write(i + "\n")

if __name__ == "__main__":

    write_file()#重点企业
    # seller_all()#去年的所有seller_id数据

