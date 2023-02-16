
set_amazon_shopgoods = set()
month = int(input("202012(除跨年):"))
last_month = month-1
#邮编
zip_dict ={}
with open(r"X:\数据库\美国亚马逊\us_seed\{地区邮编}[id,省,市,区].txt", "r", encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        zip_dict[data[0]]=(data[1:4])
sort_dict ={}
with open(r"X:\数据库\美国亚马逊\{3_3店铺分类}[id,main_sales,sort].txt", "r", encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        sort_dict[data[0]]=(data[1])
price_dict ={}
with open(r"X:\数据库\美国亚马逊\{3_2店铺单价}[id,price_avg].txt", "r", encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        price_dict[data[0]]=(data[1])
shop_file = open(r"X:\数据库\美国亚马逊\{{amazonus_shopinfo_{}}}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt".format(month),"w",encoding="utf-8")
with open(r"X:\数据库\美国亚马逊\{{amazonus_shopinfo_{}_old}}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt".format(month),"r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        if len(data) > 11:
            key = data[0]
            zip_code = data[6]
            month_comment = data[11].strip()
            if month_comment and month_comment!="0":
                set_amazon_shopgoods.add(key)
            zip = zip_dict.get(zip_code)
            province = ""
            city = ""
            county = ""
            if zip:
                province = zip[0]
                city = zip[1]
                county = zip[2]
            sort=sort_dict.get(key,"")
            price=price_dict.get(key,"")
            data[-1]=price
            data[-2]=sort
            data[-3]=county
            data[-4]=city
            data[-5]=province
            shop_file.write(",".join(data)+"\n")

with open(r"X:\数据库\美国亚马逊\amazon_shopgoods_seed.txt","w",encoding="utf-8") as f:
    for i in set_amazon_shopgoods:
        f.write("{}\n".format(i))





