# sys.path.append("F:\pycharmproject\data_process")
from tools.tools_s.sql_base import get_data
from collections import defaultdict
from unuse.data_count import main_dict_jd,main_dict_taobao

sql_prame = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql_prame_227 = {
    "host": "192.168.0.227",
    "db": "",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
taobao_price = "discount_price as price,discount_price*sales_month as sales_money"
jd_price = "price,price*realcomment/3.5 as sales_money"
pts_dict ={"tmall":"oridata_tmall","taobao":"oridata_taobao","jd":"oridata_jd"}
pts = ["tmall","jd","taobao_qiye"]
condition = " where city like '%温州%'"
#得到温州公司

goods_list = []
goods_sales = defaultdict(list)

for pt in pts:
    for i in [202005,202004,202003,202002,202001]:
        mouth = i
        goods_id = set()
        sql_shop = "select shop_id,main_sale,shop_name,company,county from {}_shopinfo_{}{}".format(pt,mouth,condition)
        shop_data = get_data(sql_prame, sql_shop)
        if pt != "jd":
            main_dict = main_dict_taobao
            price_str = taobao_price
            a = "goodsmobile"
        else:
            main_dict = main_dict_jd
            price_str = jd_price
            a="goodsinfo"
        shop_id = [i[0] for i in shop_data]
        shop_info = {}
        for i in shop_data:
            info = list(i[2:])
            info.append(main_dict.get(i[1]))
            shop_info[i[0]]=info
        sql_prame_227["db"] = pts_dict.get(pt)
        shop_ids = "','".join(shop_id)
        if pt =="taobao_qiye":
            pt_name = "taobao"
        else:
            pt_name = pt
        sql_goods = "select shop_id,goods_id,goods_name,{} from {}_{}_{} where shop_id in ('{}') ".format(price_str,pt_name,a,mouth, shop_ids)
        goods_infos = get_data(sql_prame_227, sql_goods)
        for goods_info in goods_infos:
            goods_sales[goods_info[1]].append(goods_info[4])
            if goods_info[1] not in goods_id:
                goods_info = list(goods_info)
                goods_info.extend(shop_info.get(goods_info[0]))
                goods_list.append(goods_info)
                goods_id.add(goods_info[1])
with open("test.csv","w",encoding="utf-8") as f:
    for i in goods_list:
        i[4]=sum(goods_sales.get(i[1],[]))
        f.write(",".join(i))

