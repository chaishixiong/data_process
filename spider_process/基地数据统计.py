from tools.tools_s.sql_base import get_data

sql_prame1 = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql_prame2 = {
    "host": "192.168.0.227",
    "db": "oridata_1688",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql1 = '''select {} from a1688_shopinfo_202004
where company_area like "%浙江%" '''

sql2 = '''select `卖家ID英`
from a1688_goodsmobile_202004'''

zhejiangid = get_data(sql_prame1,sql1)
shop_data = get_data(sql_prame2,sql2)
zhejiangid_set = {i[0] for i in zhejiangid}
num = 0
for i in shop_data:
    if i[0] in zhejiangid_set:
        num+=1

print("商品数量：{}".format(num))
for i in range(202001,202005):
    year = i

#月份 店铺数量 有效 浙江
