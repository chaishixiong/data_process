from tools.tools_s.sql_base import get_data
from spider_process.taobao.zz_taobao_prame import sql_prame_228,sql_prame_taobao
from collections import defaultdict

month = int(input("202012(除了1月1月要改):"))
last_month = month -1  # 这里修改

sql = "select seller_id from taobao_shopinfo_{} where province = '浙江'".format(last_month)
zhejiang_shopid_data = get_data(sql_prame_228,sql)
zhejiang_sellerid = {i[0] for i in zhejiang_shopid_data}


sql_goods = "select goods_id,seller_id,sales_month from taobao_goodsmobile_{}".format(last_month)
good_data = get_data(sql_prame_taobao,sql_goods.format())
num = 0
num_sales = 0

f_w = open(r"X:\数据库\taobao\tb_goods_seed\taobao_other_seed_{}.txt".format(month),"w",encoding="utf-8")
f_w_zhejiang = open(r"X:\数据库\taobao\tb_goods_seed\taobao_zhejiang_seed_{}.txt".format(month),"w",encoding="utf-8")

result = defaultdict(set)
for i in good_data:
    goods_id = i[0]
    seller_id = i[1]
    try:
        sales = int(i[2])
    except:
        sales = 0
    data = result.get(seller_id,[])
    if seller_id not in zhejiang_sellerid and len(data) < 2:
        f_w.write("{},{}\n".format(goods_id,seller_id))
        result[seller_id].add(goods_id)
        # pass
    # elif seller_id in zhejiang_sellerid and (len(data) < 3 or sales>10):
    # elif seller_id in zhejiang_sellerid and (len(data) < 3 or sales > 7):
    elif seller_id in zhejiang_sellerid and (len(data) < 3 or sales > 5):
        f_w_zhejiang.write("{},{}\n".format(goods_id,seller_id))
        result[seller_id].add(goods_id)

