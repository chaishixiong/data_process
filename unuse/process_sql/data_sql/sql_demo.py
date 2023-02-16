from tools.tools_s.sql_base import get_data

sql_prame = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "root",
    "port":9228,
    "password": "!NEW228World"
}
sql_prame1 = {
    "host": "192.168.0.227",
    "db": "oridata_tmall",
    "user": "root",
    "port": 9227,
    "password": "!Qnriat227pdFwpT"
}


sql = '''select seller_id from tmall_shopinfo_202010
where province like "%浙江%"'''

data = get_data(sql_prame,sql)
#处理数据格式
set_data = {i[0] for i in data}
#
del data
sql1 = '''select goods_id,seller_id,inventory,bid from tmall_goodsmobile_202010'''
data1 = get_data(sql_prame1,sql1)

#处理逻辑
print("xiazaihao")
file_name = r"X:\数据库\双十一\sales\{tmall_bid}[goods,inventory,bid].txt"
file = open(file_name,"w",encoding="utf-8")
for i in data1:
    if i[1] in set_data:
        file.write(",".join(i)+"\n")
