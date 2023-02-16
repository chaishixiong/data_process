import sys
# sys.path.append("F:\pycharmproject\data_process")
from tools.tools_s.sql_base import get_data
from collections import defaultdict
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
pts_dict ={"tmall":"oridata_tmall","taobao_qiye":"oridata_taobao","jd":"oridata_jd"}
pts = ["jd"]
condition = " where shop_id like '129065'"
main_dict_jd = {"数码":"3C数码",
"手机":"3C数码",
"家用电器":"3C数码",
"电脑、办公":"3C数码",
"手机通讯":"3C数码",
"服饰内衣":"服饰鞋包",
"鞋靴":"服饰鞋包",
"礼品箱包":"服饰鞋包",
"箱包皮具":"服饰鞋包",
"汽车用品":"机车配件",
"整车":"机车配件",
"家具":"家居家装",
"家装建材":"家居家装",
"钟表":"家居家装",
"厨具":"家居家装",
"家具家装":"家居家装",
"家居家装":"家居家装",
"家居家纺":"家居家装",
"家居日用":"家居家装",
"家纺":"家居家装",
"家具日用":"家居家装",
"家庭清洁/纸品":"家居家装",
"个护化妆":"美妆护肤",
"珠宝首饰":"美妆护肤",
"美妆个护":"美妆护肤",
"个人护理":"美妆护肤",
"美妆护肤":"美妆护肤",
"母婴":"母婴用品",
"农用物资":"其他",
"宠物生活":"其他",
"cxy":"其他",
"ASEN":"其他",
"化学制剂药":"其他",
"拍卖":"其他",
"首页":"其他",
"#N/A":"其他",
"(空白)":"其他",
"浙江省建筑工程资料填写":"其他",
"农资绿植":"其他",
"二手商品":"其他",
"海外生活":"其他",
"房地产":"其他",
"工业品":"其他",
"测试分类":"其他",
"卖家服务":"其他",
"医疗器械":"其他",
"农资园艺":"其他",
"度假":"生活服务",
"本地生活/旅游出行":"生活服务",
"酒店":"生活服务",
"票务":"生活服务",
"礼品":"生活服务",
"食品饮料":"食品保健",
"生鲜":"食品保健",
"酒类":"食品保健",
"营养保健":"食品保健",
"医药保健":"食品保健",
"处方药":"食品保健",
"养生保健":"食品保健",
"中成药":"食品保健",
"玩具乐器":"文化娱乐",
"音乐":"文化娱乐",
"影视":"文化娱乐",
"教育音像":"文化娱乐",
"图书":"文化娱乐",
"邮币":"文化娱乐",
"教育培训":"文化娱乐",
"数字内容":"文化娱乐",
"艺术品":"文化娱乐",
"文娱":"文化娱乐",
"运动户外":"运动户外",
"家用器械":"运动户外"}
main_dict_taobao = {"3C数码":"3C数码",
"大家电":"3C数码",
"手机":"3C数码",
"服饰鞋包":"服饰鞋包",
"车品配件":"机车配件",
"汽车配件":"机车配件",
"家居用品":"家居家装",
"家装家饰":"家居家装",
"珠宝/首饰":"美妆护肤",
"美容护理":"美妆护肤",
"珠宝/配饰":"美妆护肤",
"母婴":"母婴用品",
"淘宝农资":"其他",
"淘宝新行业":"其他",
"近期无经营":"其他",
"其他行业":"其他",
"行业服务市场":"其他",
"游戏/话费":"生活服务",
"生活服务":"生活服务",
"医药健康":"食品保健",
"食品/保健":"食品保健",
"收藏/爱好":"文化娱乐",
"书籍音像":"文化娱乐",
"玩乐/收藏":"文化娱乐",
"运动/户外":"运动户外",
"文体/汽车":"运动户外"}#得到温州公司

goods_list = []
goods_sales = defaultdict(list)

for pt in pts:
    print(pt)
    for i in [202005,202004,202003,202002,202001]:
        print(i)
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
with open("test.csv","a",encoding="utf-8") as f:
    for i in goods_list:
        i[4]=str(sum(goods_sales.get(i[1],[])))
        i= [j if j else "" for j in i]
        f.write(",".join(i)+"\n")
