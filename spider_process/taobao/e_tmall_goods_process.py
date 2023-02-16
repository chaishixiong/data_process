#
shop_dict = {}
month = int(input("202012(除了1月1月要改):"))
last_month = 1 if month == 12 else month-1
with open(r"X:\数据库\taobao\{3_4_天猫卖家ID}[KEY,卖家ID].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        shop_id = data[0]
        seller_id = data[1]
        shop_dict[seller_id] = shop_id

bid_dict = {}
with open(r"X:\数据库\taobao\{8_0_0_天猫商品信息}[商品ID,库存,bid].txt","r",encoding="utf-8") as f:
    num = 0
    for i in f:
        num+=1
        if num%1000000==0:
            print(num)
        data = i.strip().split(",")
        goods_id = data[0]
        inventory_id = data[1]
        bid = data[2]
        bid_dict[goods_id] = (inventory_id,bid)
file_write = open(r"X:\数据库\taobao\{{tmall_goodsmobile_{}}}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性].txt".format(month),"w",encoding="utf-8")
with open(r"X:\数据库\taobao\{taobao_look-data_tmall}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    b_type = "B"
    num = 0
    for i in f:
        try:
            num += 1
            data = i.strip().split(",")
            goods_id = data[0]
            sales_mouth = data[3]
            inventory = bid_dict.get(goods_id,["",""])[0]
            cid = data[5]
            bid = bid_dict.get(goods_id,["",""])[1]
            good_name = data[4]
            seller_id = data[1]
            shop_id = shop_dict.get(seller_id,"")
            price = data[2]
            pic = data[7]
            write_data = [""] * 27
            write_data[1] = goods_id
            write_data[3] = sales_mouth
            write_data[5] = inventory
            write_data[8] = cid
            write_data[9] = bid
            write_data[10] = b_type
            write_data[11] = good_name
            write_data[12] = seller_id
            write_data[13] = shop_id
            write_data[15] = price
            write_data[25] = pic
            file_write.write(",".join(write_data)+"\n")
            if num%1000000==0:
                print(num)
                file_write.flush()
        except Exception as e:
            pass