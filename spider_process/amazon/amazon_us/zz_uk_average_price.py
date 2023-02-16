shop_data = {}
with open(r"X:\数据库\欧洲亚马逊\{3_2shop_price}[id,price_avg].txt", "r", encoding="utf-8") as f_f:
    b_num = 0
    for i_i in f_f:
        b_num += 1
        if b_num % 1000000 == 0:
            print(b_num)
        data_1 = i_i.strip().split(",")
        g_id = data_1[0]
        price = data_1[1]
        shop_data[g_id] = price

file_write = open(r"X:\数据库\欧洲亚马逊\select_欧洲亚马逊商店详情_入库_new.txt", "a", encoding="utf-8")
with open(r"X:\数据库\欧洲亚马逊\{select_欧洲亚马逊商店详情_（入库）}[shop_name,shop_id,company,业务类型,商业登记号,增值税编号,address,评分,店铺介绍,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,main_sales,sales_money].txt", 'r', encoding="utf-8") as f:
    goods_list = {}
    num = 0
    for i in f:
        try:
            num += 1
            data = i.strip().split(",")
            goods_id = data[1]
            average_price = shop_data.get(goods_id)
            if average_price != None:
                data[26] = average_price
                file_write.write(",".join(data) + "\n")
            else:
                file_write.write(",".join(data) + "\n")
            if num % 1000000 == 0:
                print(num)
                file_write.flush()
        except Exception as e:
            print(e)
