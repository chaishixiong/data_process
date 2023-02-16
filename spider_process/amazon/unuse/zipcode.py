w_file = open(r"X:\数据库\美国亚马逊\{未匹配邮编}[邮编].txt","w",encoding="utf-8")
zip_set = set()
with open(r"X:\数据库\美国亚马逊\{amazonus_shopinfo}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.split(",")
        county = data[5]
        province = data[24].strip()
        zipcode = data[6].strip()
        if not province and zipcode and ("CN" in county or "cn" in county) and len(zipcode)==6 and zipcode not in zip_set:#
            zip_set.add(zipcode)
            w_file.write(zipcode+"\n")