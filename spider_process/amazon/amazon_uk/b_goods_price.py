from collections import defaultdict
#需要上月X:\数据库\美国亚马逊\{上月}\{{3_2店铺单价}}文件
#需要 amazon_shopgoods 商品文件

shop_dict = defaultdict(lambda :[[],[]])
month = int(input("202012(除跨年):"))
last_month = 202212
write_file=open("X:\数据库\欧洲亚马逊\{3_2店铺单价}[id,price_avg].txt","w",encoding="utf-8")
with open("X:\数据库\欧洲亚马逊\{{amazon_uk_goodsinfo_{}}}[shop_id,goods_name,comment_score,comment_num,goods_url,price,goods_id,goods_num,brand].txt".format(month),"r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        shop_id = data[0]
        try:
            comment_num = data[3]
            price = data[5]
            comment_num1 = int(comment_num) if comment_num else 0
            price1 = float(price) if price else 0
            shop_dict[shop_id][0].append(comment_num1)
            shop_dict[shop_id][1].append(comment_num1 * price1)
            # shop_dict[shop_id][2].append(shop_id)
        except:
            print(i)
amazon_id = set()
for i,y in shop_dict.items():
    totlemoney = sum(y[1])
    totlexomment = sum(y[0])
    if totlexomment:
        price_avg = (totlemoney/totlexomment) + 8
        amazon_id.add(i)
        write_file.write("{},{}\n".format(i,price_avg))
with open(r"X:\数据库\欧洲亚马逊\{}\{{3_2店铺单价}}[id,price_avg].txt".format(last_month),"r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        if data[0] not in amazon_id:
            data[1] = str(float(data[1]) + 8)
            write_file.write(i)
            amazon_id.add(data[0])
