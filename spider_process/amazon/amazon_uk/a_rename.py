import os
month = int(input("202012(除了1月1月要改):"))
last_month = month-1
os.rename(r"X:\数据库\欧洲亚马逊\amazon_uk_shopinfo.txt",r"X:\数据库\欧洲亚马逊\{{amazon_uk_shopinfo_{}_old}}[KEY,店铺名称,店铺介绍,公司,公司地址信息,国家,邮编,公司原始信息,30天好评率,30天中评率,30天差评率,30天评论数,90天好评率,90天中评率,90天差评率,90天评论数,12月好评率,12月中评率,12月差评率,12月评论数,累积好评率,累积中评率,累积差评率,累积评论数,省,市,区,main_sales,店铺单价].txt".format(month))
os.rename(r"X:\数据库\欧洲亚马逊\amazon_uk_shopgoods.txt",r"X:\数据库\欧洲亚马逊\{{amazon_uk_goodsinfo_{}}}[shop_id,goods_name,comment_score,comment_num,goods_url,price,goods_id,goods_num,brand].txt".format(month))
