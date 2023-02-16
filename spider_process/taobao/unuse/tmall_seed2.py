from tools.tools_s.sql_base import get_data
mouth = "202101"#上月的月分数
shop_ids = ["112429393"]#上月的月分数
sql = '''select goods_id,seller_id
from tmall_goodsmobile_{}
where shop_id in ("{}") limit 40'''.format(mouth,'","'.join(shop_ids))
sql_prame = {
    "host": "192.168.0.227",
    "db": "oridata_tmall",
    "user": "read",
    "password": "nriat227read@x#",
    "port":9227
}
file_tmall_zhejiang = open(r"X:\数据库\taobao\{tmall_shopid_zhejiang}[shop_id,seller_id].txt","r",encoding="utf-8")
tmall_set = {i.strip().split(",")[1]for i in file_tmall_zhejiang.readlines()}
file_tmall_zhejiang.close()
file_tmall_goods1 = open(r"X:\数据库\taobao\{5_0_0_asyn取商品ID_天猫}[商品ID,KEY].txt","r",encoding="utf-8")
tmallgood_set = {i.strip().split(",")[0] for i in file_tmall_goods1.readlines()}
file_tmall_goods1.close()


write_file = open(r"X:\数据库\taobao\{tmall_seed2}[goods,seller_id].txt","w",encoding="utf-8")
with open(r"X:\数据库\taobao\{taobao_look-data_tmall}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    num = 0
    for i in f:
        data = i.strip().split(",")
        if data[3] and int(data[3])>10 and data[1] in tmall_set and data[0] not in tmallgood_set:
            # num+=float(data[2])*int(data[3])
            write_file.write("{},{}\n".format(data[0],data[1]))
            num+=1
    print(num)
for i in get_data(sql_prame,sql):
    write_file.write("{},{}\n".format(i[0], i[1]))