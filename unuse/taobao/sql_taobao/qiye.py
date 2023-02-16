from tools.tools_s.sql_base import get_data
sql = '''select shop_id,province,city,area from taobao_qiyeshoinfo_202003'''
sql_prame = {
    "host": "192.168.0.227",
    "db": "oridata_taobao",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql2 = '''select shop_id,company,sales_count,sales_money from taobao_shopinfo_202003'''
sql_prame2 = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
data = get_data(sql_prame,sql)
data2 = get_data(sql_prame2,sql2)
dict_qiye = dict()
dict_all = dict()
for i in data2:
    if i[1]:
        dict_qiye[i[0]]=i[2:]
    dict_all[i[0]]=i[2:]

file = open(r"X:\数据库\xc\{taobao_add}[shop_id,province,city,area,sales_count,sales_money].txt","w",encoding="utf-8")
file2 = open(r"X:\数据库\xc\{taobao_all}[shop_id,province,city,area,sales_count,sales_money].txt","w",encoding="utf-8")

for i in data:
    a = list(i)
    a.extend(dict_all.get(i[0]) if dict_all.get(i[0]) else ["",""])
    file2.write(",".join(a)+"\n")
    if i[0] not in dict_qiye:
        file.write(",".join(a) + "\n")

