from tools.tools_s.sql_base import get_data
month = int(input("202012(除了1月1月要改):"))
last_month = month - 1
sql_prame = {
    "host": "192.168.1.4",
    "db": "ec_cross_border",
    "user": "update_all",
    "password": "123456",
    "port":3306
}
key_data = get_data(sql_prame,'''select distinct (`key`) from alibabagj_shopinfo_{}'''.format(last_month))
key_set = {i[0] for i in key_data}
with open("X:\数据库\阿里巴巴国际站\{alibabagj_shopid_info}[key,供应商名称,供应商url,供应商6个月销售额,供应商6个月销量,供应商提供年数,供应商出口主要国家,供应商的贸易保证限额,供应商的交易等级,供应商回复时间,供应商回复率,供应商国家,供应商省,供应商产品url,评论分数,评论数,评论url].txt","r",encoding="utf-8") as f:
    for i in f:
        key = i.split(",")[0]
        key_set.add(key)
with open(r"X:/数据库/阿里巴巴国际站/alibabagj_shop_seed.txt","w",encoding="utf-8") as f:
    for i in key_set:
        f.write(i+"\n")
