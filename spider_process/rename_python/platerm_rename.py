# coding: utf-8
import os
month = int(input("202012(除了1月1月要改):"))
last_month = month-1
# os.rename(r"X:\数据库\scrapy采集平台\jd_id.txt",r"X:\数据库\scrapy采集平台\{{jdid_goodsinfo_{}}}[vender_id,total_num,comment_num,comment_score,img_url,promo_statu,goods_id,goods_name].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\jd_idshop_info.txt",r"X:\数据库\scrapy采集平台\{{jdid_shopinfo_{}}}[vender_id,shop_name,fans,categorys,goods_num].txt".format(month))
os.rename(r"X:\数据库\scrapy采集平台\newegg_goods.txt_去重.txt",r"X:\数据库\scrapy采集平台\{{newegg_goodsinfo_{}}}[sort,url,name,brand,price,goods_id,size,type,color,age,shop_url,shop_name].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\shopee_goodlist.txt",r"X:\数据库\scrapy采集平台\{{shopee_goodsinfo_{}}}[shop_id,goods_id,name,price,currency,totle_num,sales_num,stock,rating_star,item_status,show_free_shipping,brand,cid,url,location,view_count].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\shopee_good店铺信息.txt",r"X:\数据库\scrapy采集平台\{{shopee_shopinfo_{}}}[shop_id,name,description,country,place,follower_count,rating_good,rating_bad,cancellation_rate,url,item_count,rating_star,shop_location].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\shopee_sort.txt",r"X:\数据库\scrapy采集平台\{{shopee_sortinfo_{}}}[cid,cname,cid2,cname2,cid3,cname3].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\xiecheng.txt_去重.txt",r"X:\数据库\scrapy采集平台\{{xiecheng_shopinfo_{}}}[hotel_num,hotel_id,hotel_name,hotel_enname,price,city,address,comment_num,comment].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\gmarket_spidershopinfo.txt",r"X:\数据库\scrapy采集平台\{{gmarket_shopinfo_{}}}[shop_id,shop_name,shop_url,boss,phone,fax,num,email,address].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\gmarket_spider.txt",r"X:\数据库\scrapy采集平台\{{gmarket_goodinfo_{}}}[shop_id,goods_id,goods_name,goods_url,price,yunfei,comment,sales_count].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\linio_spidershopinfo.txt_去重.txt",r"X:\数据库\scrapy采集平台\{{linio_shopinfo_{}}}[good_id,shop_name,shop_url,shop_score,cat3].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\linio_spider.txt",r"X:\数据库\scrapy采集平台\{{linio_goodsinfo_{}}}[shop_name,good_id,good_name,brand,good_score,price,comment,cat1,cat2,cat3,cat4].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\kilimall_spidershopinfo.txt_去重.txt",r"X:\数据库\scrapy采集平台\{{kilimall_shopinfo_{}}}[shop_url,shop_id,shop_name,score,category].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\kilimall_spider.txt",r"X:\数据库\scrapy采集平台\{{kilimall_goodsinfo_{}}}[goods_id,good_url,good_name,new_price,old_price,shop_id,comment_nums,category].txt".format(month))
# os.rename(r"X:\数据库\ebay数据采集\ebayinfo_goods.txt",r"X:\数据库\ebay数据采集\{{ebay_goodsinfo_{}}}[商品ID,商品名称,单价(美元),单价(RMB),项目地点,品牌,卖家用户名,销售量,类目1,类目2,类目3,类目4,类目5,类目6].txt".format(month))
# os.rename(r"X:\数据库\ebay数据采集\{3_1_ebay_店铺详情(可入库)}[卖家用户名,此用户在ebay粉丝数,国家,好评率,评论评分,描述评分,交流评分,物流评分,运费评分,卖家描述,好评数,中评数,差评数,点击量,此用户在ebay的评论数,商品数,入驻时间,店铺链接].txt",r"X:\数据库\ebay数据采集\{{ebay_usrinfo_{}}}[卖家用户名,此用户在ebay粉丝数,国家,好评率,评论评分,描述评分,交流评分,物流评分,运费评分,卖家描述,好评数,中评数,差评数,点击量,此用户在ebay的评论数,商品数,入驻时间,店铺链接].txt".format(month))
# os.rename(r"X:\数据库\scrapy采集平台\fruugo_good.txt",r"X:\数据库\scrapy采集平台\{{fruugo_goodsinfo_{}}}[key,good_name,price,shop_name,shop_url,brand,category,size,goods_id,ean,retailer_vrn,colour,description].txt".format(month))

