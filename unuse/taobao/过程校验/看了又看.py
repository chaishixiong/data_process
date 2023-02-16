path = r"D:\data_process\taobao10过程校验"
w_file = path+"\kanleyoukna结果.txt"
r_file_seed = path+r"\{zj_exp}[卖家ID,店铺ID,商品ID].txt"
r_file_taobao = path+r"\{zjtaobao}[sell,shop,item].txt"
r_file_tmall = path+r"\{zjtmall}[sell,shop,item].txt"

seed_shopid = set()
seed_itemid = set()
with open(r_file_seed,"r",encoding="utf-8") as f_r:
    num1 = 1
    for i in f_r.readlines():
        if num1 % 1000000 == 0:
            print(num1)
        num1 += 1
        str_list = i.strip().split(",")
        shop_id = str_list[1]
        item_id = str_list[2]
        seed_shopid.add(shop_id)
        seed_itemid.add(item_id)

taobao_shopid = set()
taobao_itemid = set()
tmall_shopid = set()
tmall_itemid = set()
with open(r_file_taobao,"r",encoding="utf-8") as f_r:
    num1 = 1
    for i in f_r.readlines():
        if num1 % 1000000 == 0:
            print(num1)
        num1 += 1
        str_list = i.strip().split(",")
        shop_id = str_list[1]
        item_id = str_list[2]
        taobao_shopid.add(shop_id)
        taobao_itemid.add(item_id)

with open(r_file_tmall,"r",encoding="utf-8") as f_r:
    num1 = 1
    for i in f_r.readlines():
        if num1 % 1000000 == 0:
            print(num1)
        num1 += 1
        str_list = i.strip().split(",")
        shop_id = str_list[1]
        item_id = str_list[2]
        tmall_shopid.add(shop_id)
        tmall_itemid.add(item_id)


shuchu_shop_id = len(seed_shopid)
shuchu_item_id = len(seed_itemid)
shuchu_taobao_shopid = len(taobao_shopid)
shuchu_taobao_itemid = len(taobao_itemid)
shuchu_tmall_shopid = len(tmall_shopid)
shuchu_tmall_itemid = len(tmall_itemid)
file = open(w_file,"a+",encoding="utf-8")
file.write("\n")
file.write("种子shop_id："+str(shuchu_shop_id)+"\n")
file.write("种子item_id："+str(shuchu_item_id)+"\n")
file.write("原淘宝shop_id："+str(shuchu_taobao_shopid)+"\n")
file.write("原淘宝item_id："+str(shuchu_taobao_itemid)+"\n")
file.write("原天猫shop_id："+str(shuchu_tmall_shopid)+"\n")
file.write("原天猫item_id："+str(shuchu_tmall_itemid)+"\n")
file.write("种子-淘宝shop_id："+str(len(seed_shopid-taobao_shopid))+"\n")
file.write("种子-淘宝item_id："+str(len(seed_itemid-taobao_itemid))+"\n")
file.write("种子-天猫shop_id："+str(len(seed_shopid-tmall_shopid))+"\n")
file.write("种子-天猫item_id："+str(len(seed_itemid-tmall_itemid))+"\n")
file.write("种子-taobao-天猫shop_id："+str(len(seed_shopid-taobao_shopid-tmall_shopid))+"\n")
file.write("taobao&天猫shop_id-种子："+str(len(taobao_shopid&tmall_shopid-seed_shopid))+"\n")
file.write("种子-taobao-天猫item_id："+str(len(seed_itemid-taobao_itemid-tmall_itemid))+"\n")
file.write("taobao&天猫item_id-种子："+str(len(taobao_itemid&tmall_itemid-seed_itemid))+"\n")



