taobao_id = set()
with open(r"X:\数据库\taobao\{3_4_天猫卖家ID}[KEY,卖家ID].txt","r",encoding="utf-8") as f:
    for i in f:
        seller_id = i.strip().split(",")[1]
        taobao_id.add(seller_id)
with open(r"X:\数据库\taobao\{3_6_淘宝卖家ID}[KEY,卖家ID].txt","r",encoding="utf-8") as f:
    for i in f:
        seller_id = i.strip().split(",")[1]
        taobao_id.add(seller_id)
print("上月种子生成")
seller = set()
with open(r"X:\数据库\taobao\{taobao_look-data_tmall}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    for i in f:
        seller_id = i.strip().split(",")[1]
        if seller_id not in taobao_id:
            seller.add(seller_id)
print("tmall中有{}".format(len(seller)))
with open(r"X:\数据库\taobao\{taobao_look-data_zhejiang}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    for i in f:
        seller_id = i.strip().split(",")[1]
        if seller_id not in taobao_id:
            seller.add(seller_id)
print("淘宝浙江中有{}".format(len(seller)))
with open(r"X:\数据库\taobao\{taobao_look-data_other_all}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    for i in f:
        try:
            seller_id = i.strip().split(",")[1]
            if seller_id not in taobao_id:
                seller.add(seller_id)
        except Exception as e:
            print(i)
print("淘宝其他中有{}".format(len(seller)))
with open(r"X:\数据库\taobao\{taobao_look_new_seller}[seller_id].txt","a",encoding="utf-8") as f:
    for i in seller:
        f.write("{}\n".format(i))
