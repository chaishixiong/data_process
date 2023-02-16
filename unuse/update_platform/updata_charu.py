#匹配softtime
import pymysql

host = "192.168.0.227"
port = 3306
db = "ec_cross_company"
db2 = "ec_cross_border"
name = "dev"
password = "Data227or8Dev715#"


def get_data(connect,sql_select):
    cursor = connect.cursor()
    num = cursor.execute(sql_select)
    headers = cursor.description
    data = cursor.fetchall()#匹配表里的data
    return data,num,headers
connect1 = pymysql.connect(host=host,port=port,db=db2,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
sql_select = '''select sum(reviews*price_lod),sum(reviews*price_now),seller_id from lazadacoid_goodsinfo_201909 group by seller_id limit 10;'''
data,num,headers = get_data(connect1,sql_select)
connect1.close()

connect = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)
sql_select1 = '''select * from lazadacoid_shopinfo_201909 limit 10'''
data1,num1,headers1 = get_data(connect,sql_select1)
connect.close()
sql_update = '''UPDATE smt_shopinfo_201904 set province_match = "{}",city_match = "{}",area_match= "{}"
where shop_name = "{}"'''

insert_sql = "insert into alibabagj_shopinfo_201908 ({})values ({});"

delect_sql = '''delete from alibabagj_shopinfo_201908 where `index_num` ={}'''

all_data = cursor1.fetchall()
title_list = []
for i in headers1:
    title_list.append(i[0])
# title_list.pop(-1)#去除更新时间



print_num = 0
for one_data in data1:

    print(print_num)
    print_num += 1
    data_list = []

    for i in one_data:
        if i is None:
            i = "Null"
        else:
            i = '"'+pymysql.escape_string(str(i))+'"'
        data_list.append(i)


    shop_name_all = one_data[0]#shop_name的位置这里写死了
    index_num = one_data[-1]
    platform_all = one_data.get("platform")

    for dizhi_dict in data:
        shop_name = dizhi_dict.get("shop_name")
        # platform = dizhi_dict.get("platform")
        province_match = dizhi_dict.get("province_match")
        province_match = '"'+province_match+'"' if province_match else "Null"
        city_match = dizhi_dict.get("city_match")
        city_match = '"'+city_match+'"' if city_match else "Null"
        area_match = dizhi_dict.get("area_match")
        area_match = '"'+area_match+'"' if area_match else "Null"

        if shop_name_all == shop_name: #and platform_all == platform:
            data_list[-4] = province_match
            data_list[-3] = city_match
            data_list[-2] = area_match
            data_list.pop(-1)

            clumns = ",".join(title_list)
            value_str = ",".join(data_list)
            sql_insert = insert_sql.format(clumns,value_str)
            sql_delect = delect_sql.format(index_num)

            cursor.execute(sql_insert)
            cursor.execute(sql_delect)
            break
