from tools.tools_s.sql_base import get_data

sql_prame_227 = {
    "host": "192.168.0.227",
    "db": "",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql_prame = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}


sql_prame_taobao = sql_prame_227
sql_prame_taobao["db"]="oridata_taobao"
sql = "select shop_id from taobao_qiyeinfo_202006 where county like '%鄞州%'"
data = get_data(sql_prame_taobao,sql)


sql_prame_mouth = sql_prame
sql2 = "select shop_id from taobao_qiye_shopinfo_202006 where county like '%鄞州%'"
data2 = get_data(sql_prame_mouth,sql2)
data_set_1 = {i[0]for i in data}
data_set_2 = {i[0]for i in data2}

shop_id = data_set_1-data_set_2
shop_str = "','".join(shop_id)
condition = "where shop_id in ('{}')".format(shop_str)
sql3 = "select * from taobao_shopinfo_202006 {}".format(condition)

data3 = get_data(sql_prame,sql3)
with open(r"C:\Users\Administrator\Desktop\鄞州.csv","w",encoding="gbk") as f:
    for i in data3:
        f.write(",".join([j if j else "" for j in i])+"\n")
