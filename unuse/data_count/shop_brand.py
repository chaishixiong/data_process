from tools.tools_s.sql_base import get_data
from collections import defaultdict
import re
sql_prame_228 = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql_prame_tmall = {
    "host": "192.168.0.227",
    "db": "oridata_tmall",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql_prame_taobao = {
    "host": "192.168.0.227",
    "db": "oridata_taobao",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql_prame_jd = {
    "host": "192.168.0.227",
    "db": "oridata_jd",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
def get_shuju():
    platforms = ["taobao_qiye"]
    mouths = list(range(201901,201907))
    for platform in platforms:
        #先得到浙江的shop_id
        file = open("{}2019.txt".format(platform),"a",encoding="utf-8")
        sort_dict = defaultdict(lambda:defaultdict(list))
        cid_dict = get_cid(platform)
        shop_dict = {}
        for mouth in mouths:
            sql = '''select seller_id,shop_fans_num,0 from {}_shopinfo_{} where province = '浙江省' '''.format(platform,mouth)#jd
            zhejiang_shop = get_data(sql_prame_228,sql)
            zhejing_xiu = []
            for i in zhejiang_shop:
                if "&" in i[0]:
                    a = re.sub("&.*","",i[0])
                    zhejing_xiu.append((a,i[1],i[2]))
                else:
                    zhejing_xiu.append(i)
            print("{},{}店铺sql".format(platform,mouth))
            shop_dict.update({i[0]:[i[1],i[2]] for i in zhejing_xiu})
            shop_ids = ",".join({i[0] for i in zhejing_xiu})
            if platform=="tmall":
                sql_goods = '''select goods_id,seller_id,bid,cid,sales_month,discount_price,comment_count from {}_goodsmobile_{} where seller_id in ({})'''.format(
                    platform, mouth, shop_ids)
                zhejiang_goods = get_data(sql_prame_tmall,sql_goods)
            elif platform=="taobao_qiye":
                sql_goods = '''select goods_id,seller_id,bid,cid,sales_month,discount_price,comment_count from taobao_goodsmobile_{} where seller_id in ({})'''.format(
                     mouth, shop_ids)
                zhejiang_goods = get_data(sql_prame_taobao,sql_goods)
            else:
                sql_goods = '''select goods_id,shop_id,brand_name,CID3,realcomment,price,realcomment from {}_goodsinfo_{} where shop_id in ({})'''.format(
                    platform, mouth, shop_ids)
                zhejiang_goods = get_data(sql_prame_jd,sql_goods)
            print("{},{}商品sql".format(platform,mouth))
            for i in zhejiang_goods:
                if i[3] in cid_dict:
                    sort_dict[cid_dict.get(i[3])][i[2]].append(i)
                    file.write("{},{}\n".format(cid_dict.get(i[3]),",".join(i)))
            file.flush()
        data_process(sort_dict,shop_dict)
def data_process(sort_dict,shop_dict):
    zhibo=get_zhibo()
    with open("taobao_jieguo2019.txt","w",encoding="utf-8") as f:
        for cid in sort_dict:
            bid_dict = sort_dict.get(cid)
            for bid in bid_dict:
                goodsinfo = bid_dict.get(bid)
                goods_num = len(goodsinfo)
                shop_ids = {i[1]for i in goodsinfo}#卖家id
                shop_num = len(shop_ids)
                shop_fans = []
                shop_rate = []
                shop_zhibo = []
                for shop_id in shop_ids:
                    fans_str = shop_dict.get(shop_id)[0]
                    if fans_str:
                        if "万" in fans_str:
                            fans = int(float(fans_str.replace("万",""))*10000)
                        else:
                            try:
                                fans = int(fans_str)
                            except:
                                fans = 0
                        shop_fans.append(fans)
                    rate = shop_dict.get(shop_id)[1]
                    try:
                        rate = float(rate)
                    except:
                        rate = 0
                    if rate:
                        shop_rate.append(rate)
                    if zhibo.get(shop_id):
                        shop_zhibo.append(int(zhibo.get(shop_id)))
                comment = sum([int(i[6]) for i in goodsinfo if i[6]])
                rate=0
                bad_rate = 0
                if len(shop_rate):
                    rate = sum(shop_rate)/len(shop_rate)/5
                    bad_rate = int(comment*(1-rate))
                fans_t = sum(shop_fans)
                money_list = []
                for i in goodsinfo:
                    if i[4] and i[5]:
                        try:
                            money = float(i[4]) * float(i[5])
                        except:
                            a = i[4].replace("+","")
                            if "万" in a:
                                a = int(float(a.replace("万", "")) * 10000)
                            money = float(a) * float(i[5])
                        money_list.append(money)
                sales_money = sum(money_list)
                zhibo_num = sum(shop_zhibo)
                a = "{},{},{},{},{},{},{},{},{}\n".format(cid,bid,shop_num,fans_t,goods_num,sales_money,rate,bad_rate,zhibo_num)
                f.write(a)
# def file_dict():
#     sort_dict = defaultdict(lambda: defaultdict(list))
#     with open("taobao_qiye.txt","r",encoding="utf-8")as f:
#         for i in f:
#             data = i.strip().split(",")
#             sort_dict[data[0]][data[3]].append((data[1:]))
#     data_process(sort_dict, shop_dict)


def get_cid(platform):
    sort_dict = dict()
    if platform == "tmall" or platform == "taobao_qiye":
        with open(r"C:\Users\Administrator\Desktop\cid_tmall.txt","r",encoding="utf-8") as f:
            for i in f:
                data = i.strip().split(",")
                cid = data[0]
                sort = data[1]
                sort_dict[cid]=sort
        return sort_dict
    else:
        with open(r"C:\Users\Administrator\Desktop\cid_jd.txt","r",encoding="utf-8") as f:
            for i in f:
                data = i.strip().split(",")
                cid = data[0]
                sort = data[1]
                sort_dict[cid] = sort
        return sort_dict
def get_zhibo():
    sql = '''select anchor_id,live_count from livingtaobao_showinfo_202008
GROUP BY anchor_id'''
    data = get_data(sql_prame_taobao,sql)
    data = {i[0] : i[1] for i in data}
    return data

# a = get_cid("tmall")
# b = get_cid("jd")
# a = get_zhibo()
# print(1)


get_shuju()


