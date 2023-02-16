from tools.tools_s.sql_base import get_data
#需要  销量评论比
#需要先入库
sql_prame = {
    "host": "192.168.1.4",
    "db": "ec_cross_border",
    "user": "update_all",
    "password": "123456",
    "port":3306
}
#拿平均价格
month = int(input("202012(除了1月1月要改):"))


sql ='''select a.main_sales,a.totol_money/b.totle_num from
(select main_sales,sum(comment_total*average_price) as totol_money from amazonus_shopinfo_{}
GROUP BY main_sales) as a
join
(select main_sales,sum(comment_total) as totle_num  from amazonus_shopinfo_{}
where average_price != ""
GROUP BY main_sales) as b 
on a.main_sales = b.main_sales'''.format(month,month)
data = get_data(sql_prame,sql)
price_dict = {}
for i in data:
    key = i[0]
    if not key:
        key = "other"
    price_dict[key]=i[1] + 8

#拿月度和年度评论比例
sql_year ='''select sum(comment_year)/sum(comment_month) from amazonus_shopinfo_{}'''.format(month)
data_year = get_data(sql_prame,sql_year)
year_bili = data_year[0][0]

sql ='''select a.main_sales,a.totol_money/b.totle_num from
(select main_sales,sum(comment_total*average_price) as totol_money from amazonus_shopinfo_{}
GROUP BY main_sales) as a
join
(select main_sales,sum(comment_total) as totle_num  from amazonus_shopinfo_{}
where average_price != ""
GROUP BY main_sales) as b 
on a.main_sales = b.main_sales'''.format(month, month)
data = get_data(sql_prame, sql)
#拿销评比
bili_dict = {}
with open(r"X:\数据库\美国亚马逊\us_seed\销量评论比.txt","r",encoding="utf-8") as f:
    for i in f:
        data_i = i.strip().split(",")
        bili_dict[data_i[0]]=(data_i[1],data_i[2])
file_write = open(r"X:\数据库\美国亚马逊\{{amazonus_shopinfo_{}_sales}}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始html,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价,sales,sales_money,sales_y,sales_money_y].txt".format(month),"w",encoding="utf-8")
with open(r"X:\数据库\美国亚马逊\amazonus_shopinfo_202301[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt".format(month),"r",encoding="utf-8") as f:
    num = 0
    for i in f:
        amazon_data = i.strip().split(",")
        if len(amazon_data) >= 29:
            comment_month= amazon_data[11] # 月评论数
            comment_year= amazon_data[19]  # 年评论数
            comment_totle= amazon_data[23]  # 累积评论数
            main_sales = amazon_data[27]  # main_sales
            average_price = amazon_data[28]  # 店铺单价
            sales=""
            sales_money=""
            sales_year=""
            sales_money_year=""
            if comment_totle:
                if not main_sales:
                    main_sales = "other"
                if not average_price:
                    average_price = price_dict.get(main_sales)
                if "锛?" in comment_month or "锛?" in comment_totle or "锛?" in comment_year:
                    comment_month = comment_month.replace("锛?","0")
                    comment_totle = comment_totle.replace("锛?","0")
                    comment_year = comment_year.replace("锛?","0")
                sales = int((int(comment_totle)*float(bili_dict.get(main_sales)[0])+int(comment_month)*float(bili_dict.get(main_sales)[1]))/2)
                sales_money = sales*float(average_price)
                a = bili_dict.get(main_sales)[0]
                b = bili_dict.get(main_sales)[1]
                sales_year = int((int(comment_totle)*float(bili_dict.get(main_sales)[0])+int(comment_year)/year_bili*float(bili_dict.get(main_sales)[1]))/2*year_bili)
                sales_money_year = sales_year*float(average_price)
                if sales>sales_year:
                    print(i)
            file_write.write(i.strip()+",{},{},{},{}\n".format(sales,sales_money,sales_year,sales_money_year))
