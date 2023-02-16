from collections import defaultdict
shop_dict = defaultdict(lambda :[[],[]])
write_file=open(r"X:\数据库\欧洲亚马逊\{3_2shop_price}[id,price_avg].txt","a",encoding="utf-8")
shop_id_set = set()
with open(r"X:\数据库\欧洲亚马逊\{select_欧洲亚马逊商品详情_（入库）}[seller_id,商品id,商品名称,评分,评论数量,价格].txt",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        shop_id = data[0]
        comment_num = data[-2]
        # price = data[-1]
        price = data[-1].strip('拢').strip('1锛?').strip('2锛?').strip('3锛?').strip('4锛?').strip('5锛?').strip('6锛?').strip('7锛?').strip('8锛?').strip('9锛?').strip('0锛?')
        comment_num1 = comment_num.replace("，","")
        price1 = price.replace("US$","")
        price1 = price1.replace("$","")
        price1 = price1.replace("，","")
        price1 = price1.replace("£","")
        try:
            comment_num1 = int(comment_num1) if comment_num1 else 0
            price1 = float(price1) if price1 else 0
            shop_dict[shop_id][0].append(comment_num1)
            shop_dict[shop_id][1].append(comment_num1 * price1)
        except:
            print(shop_id)
            print(price)
            pass

# print(shop_dict)
for i,y in shop_dict.items():
    totlemoney = sum(y[1])
    totlexomment = sum(y[0])
    if totlexomment and i not in shop_id_set:
        shop_id_set.add(i)
        write_file.write("{},{}\n".format(i,totlemoney/totlexomment))
with open(r"X:\数据库\欧洲亚马逊\uk_seed\{3_2shop_price}[id,price_avg].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.split(",")
        if data[0] not in shop_id_set:
            write_file.write(i)
