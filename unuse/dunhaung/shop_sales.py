
from collections import defaultdict
path = "X:\数据库\敦煌数据采集"
file ="\{dhgate_goodsinfo_202002}[店铺id,商品id,商品评论数,商品列表的销量,商品名称,商品价格_较低值,商品价格_较高值,一级类目,二级类目,三级类目,四级类目,商品id_加密,卖家id_加密,订单数,商品链接].txt"
# data_type = defaultdict(list)
# data_type2 = defaultdict(list)
data_dict = defaultdict(defaultdict)
# b = defaultdict(list)
# a = [1,2,3,4,5]
# for i in a:
#     b = defaultdict(list)
#     b["sale"].append("1")
#     data[i] =b

with open(path+file,"r",encoding="utf-8") as f:
    good_num = 0
    correct = 0
    shopid_set =set()
    for i in f:
        good_num+=1
        data = i.strip().split(",")
        if len(data) == 15:
            shop_id = data[0]
            price_max = data[6]
            price_min = data[5]
            num = data[3]
            price = price_max if price_max else price_min
            if price:
                good_num += 1
                if num:
                    try:
                        good_num += 1
                        goods_sales = float(price)*int(num)
                        if shop_id not in shopid_set:
                            shopid_set.add(shop_id)
                            a = defaultdict(list)
                            data_dict[shop_id] = a
                        data_dict[shop_id]["sale"].append(num)
                        data_dict[shop_id]["sales_money"].append(goods_sales)
                    except:
                        print(good_num)
                        print("价格格式错误",i)
            else:
                print("价格销量少了：",i)
        else:
            print(i)
    print("总数：{}错误：{}".format(good_num,int(good_num)-int(correct)),)
# salsnum = sum(lambda)lambda

