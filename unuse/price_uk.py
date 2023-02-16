from collections import defaultdict
shop_dict = defaultdict(lambda :[[],[]])
write_file=open(r"X:\数据库\欧洲亚马逊\{3_2shop_price}[id,price_avg].txt","w",encoding="utf-8")
with open(r"X:\数据库\欧洲亚马逊\{select_欧洲亚马逊商品详情_（入库）}[seller_id,商品id,商品名称,评分,评论数量,价格].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        shop_id = data[0]
        comment_num = data[4]
        price = data[5]
        comment_num1 = comment_num.replace("，","")
        price1 = price.replace("US$","")
        price1 = price1.replace("$","")
        price1 = price1.replace("，","")
        try:
            comment_num1 = int(comment_num1) if comment_num1 else 0
            price1 = float(price1) if price1 else 0
            shop_dict[shop_id][0].append(comment_num1)
            shop_dict[shop_id][1].append(comment_num1 * price1)
        except:
            print(i)

for i,y in shop_dict.items():
    totlemoney = sum(y[1])
    totlexomment = sum(y[0])
    if totlexomment:
        write_file.write("{},{}\n".format(i,totlemoney/totlexomment))