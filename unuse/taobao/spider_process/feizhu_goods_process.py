shop_dict = {}
with open(r"X:\数据库\飞猪\{3_7_飞猪卖家ID_all}[KEY,卖家ID,状态,shopUrl天猫,url天猫,飞猪].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.split(",")
        shop_id = data[0]
        seller_id = data[1]
        shop_dict[seller_id] = shop_id

file_write = open(r"X:\数据库\飞猪\{feizhu_goodsmobile_202010}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性].txt","w",encoding="utf-8")
with open(r"X:\数据库\飞猪\{feizhu_look_data}[goods,seller_id,price,sales,name,cid,score,url].txt","r",encoding="utf-8") as f:
    b_type = "F"
    num = 0
    for i in f:
        num+=1
        data = i.strip().split(",")
        goods_id = data[0]
        sales_mouth = data[3]
        cid = data[5]
        good_name = data[4]
        seller_id = data[1]
        shop_id = shop_dict.get(seller_id,"")
        price = data[2]
        pic = data[7]
        write_data = [""] * 27
        write_data[1] = goods_id
        write_data[3] = sales_mouth
        write_data[8] = cid
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


