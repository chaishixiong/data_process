from tools.tools_s.sql_base import get_data

#店铺的常用
platforms = ["tmall","jd","taobao"]
sql_prame_228 = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
#商品表常用
pts_db ={"tmall":"oridata_tmall","taobao":"oridata_taobao","jd":"oridata_jd"}
sql_prame_227 = {
    "host": "192.168.0.227",
    "db": "",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
#sql
sql = "select shop_id,sales_money from {}_shopinfo_{}{}"
condition = " where province like '%浙江%'"

shop_num = set()
shop_active = set()
shop_active_tmall = set()
shop_active_taobao = set()

for platform in platforms:
    for i in range(201901,201913):
        sql_str = sql.format(platform,i,condition)
        data=get_data(sql_prame_228,sql_str)
        for j in data:
            if j[1] and float(j[1])>0:
                if platform=="taobao":
                    shop_active_taobao.add(j[0])
                if platform=="tmall":
                    shop_active_tmall.add(j[0])
                shop_active.add(j[0])
            shop_num.add(j[0])
print("店铺：", len(shop_num))
print("活跃店铺：",len(shop_active))
print("天猫活跃店铺：",len(shop_active_tmall))
print("淘宝活跃店铺：",len(shop_active_taobao))





