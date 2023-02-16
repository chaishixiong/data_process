import os
month = int(input("202012(除了1月1月要改):"))
last_month = month-1
os.rename(r"X:\数据库\阿里巴巴国际站\alibabagj_sortgoods_合并.txt",r"X:\数据库\阿里巴巴国际站\{{alibabagj_goodsinfo_{}}}[商品url,商品名称,商品id,最低价,最高价,最小订单数,供应商名称,供应商url,供应商出口主要国家,评论分数,评论数].txt".format(month))
os.rename(r"X:\数据库\阿里巴巴国际站\alibabagj_sortshop_合并.txt_去重.txt",r"X:\数据库\阿里巴巴国际站\{alibabagj_shopid_info}[key,供应商名称,供应商url,供应商6个月销售额,供应商6个月销量,供应商提供年数,供应商出口主要国家,供应商的贸易保证限额,供应商的交易等级,供应商回复时间,供应商回复率,供应商国家,供应商省,供应商产品url,评论分数,评论数,评论url].txt")
