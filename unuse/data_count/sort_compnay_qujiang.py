from tools.tools_s.sql_base import get_data
from collections import defaultdict
# from data_process.pandas_data.main_sales import main_dict_jd,main_dict_taobao

sql_prame = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}

main_dict_jd = {"数码":"3C数码",
"手机":"3C数码",
"家用电器":"3C数码",
"电脑、办公":"3C数码",
"手机通讯":"3C数码",
"服饰内衣":"服饰鞋包",
"鞋靴":"服饰鞋包",
"礼品箱包":"服饰鞋包",
"箱包皮具":"服饰鞋包",
"汽车用品":"机车配件",
"整车":"机车配件",
"家具":"家居家装",
"家装建材":"家居家装",
"钟表":"家居家装",
"厨具":"家居家装",
"家具家装":"家居家装",
"家居家装":"家居家装",
"家居家纺":"家居家装",
"家居日用":"家居家装",
"家纺":"家居家装",
"家具日用":"家居家装",
"家庭清洁/纸品":"家居家装",
"个护化妆":"美妆护肤",
"珠宝首饰":"美妆护肤",
"美妆个护":"美妆护肤",
"个人护理":"美妆护肤",
"美妆护肤":"美妆护肤",
"母婴":"母婴用品",
"农用物资":"其他",
"宠物生活":"其他",
"cxy":"其他",
"ASEN":"其他",
"化学制剂药":"其他",
"拍卖":"其他",
"首页":"其他",
"#N/A":"其他",
"(空白)":"其他",
"浙江省建筑工程资料填写":"其他",
"农资绿植":"其他",
"二手商品":"其他",
"海外生活":"其他",
"房地产":"其他",
"工业品":"其他",
"测试分类":"其他",
"卖家服务":"其他",
"医疗器械":"其他",
"农资园艺":"其他",
"度假":"生活服务",
"本地生活/旅游出行":"生活服务",
"酒店":"生活服务",
"票务":"生活服务",
"礼品":"生活服务",
"食品饮料":"食品保健",
"生鲜":"食品保健",
"酒类":"食品保健",
"营养保健":"食品保健",
"医药保健":"食品保健",
"处方药":"食品保健",
"养生保健":"食品保健",
"中成药":"食品保健",
"玩具乐器":"文化娱乐",
"音乐":"文化娱乐",
"影视":"文化娱乐",
"教育音像":"文化娱乐",
"图书":"文化娱乐",
"邮币":"文化娱乐",
"教育培训":"文化娱乐",
"数字内容":"文化娱乐",
"艺术品":"文化娱乐",
"文娱":"文化娱乐",
"运动户外":"运动户外",
"家用器械":"运动户外"}
main_dict_taobao = {"3C数码":"3C数码",
"大家电":"3C数码",
"手机":"3C数码",
"服饰鞋包":"服饰鞋包",
"车品配件":"机车配件",
"汽车配件":"机车配件",
"家居用品":"家居家装",
"家装家饰":"家居家装",
"珠宝/首饰":"美妆护肤",
"美容护理":"美妆护肤",
"珠宝/配饰":"美妆护肤",
"母婴":"母婴用品",
"淘宝农资":"其他",
"淘宝新行业":"其他",
"近期无经营":"其他",
"其他行业":"其他",
"行业服务市场":"其他",
"游戏/话费":"生活服务",
"生活服务":"生活服务",
"医药健康":"食品保健",
"食品/保健":"食品保健",
"收藏/爱好":"文化娱乐",
"书籍音像":"文化娱乐",
"玩乐/收藏":"文化娱乐",
"运动/户外":"运动户外",
"文体/汽车":"运动户外"}

platforms = ["tmall"]
# platforms = ["jd"]
# platforms = ["taobao_qiye"]

for platform in platforms:
    for years in [2019]:

        print(years)
        print(platform)
        if platform=="jd":
            main_dict = main_dict_jd
        else:
            main_dict = main_dict_taobao
        if years==2020:
            a= list(range(202001,202007))
        else:
            # 前半年
            a= list(range(years*100+1,years*100+7))

            # #全年
            # a = list(range(years*100+1,years*100+13))
        dict_sort = defaultdict(list)

        # dict_sort_zhejiang = defaultdict(list)

        shop_totle = set()
        shop_active = set()
        company = set()

        for year in a:
            print(year)
            if platform=="jd":
                sql = "select main_sale,shop_id,sales_count*1 as sales_count,sales_money*1 as sales_money,company from {}_shopinfo_{} where county like'%衢江%'".format(platform,year)
            elif platform=="taobao":
                sql = "select main_sale,shop_id,sales_count*1 as sales_count,sales_money*1 as sales_money,company from {}_shopinfo_{} where county like'%衢江%'".format(platform,year)
            else:
                sql = "select main_sale,shop_id,sales_count*1 as sales_count,sales_money*1 as sales_money,company from {}_shopinfo_{} where county like'%衢江%'".format(platform,year)

            data = get_data(sql_prame,sql)
            for i in data:
                main_sale = main_dict.get(i[0])
                if not main_sale:
                    main_sale = "其他"
                dict_sort[main_sale].append(i[1:])
                shop_totle.add(i[1])
                if i[3] and i[3]>0:
                    shop_active.add(i[1])
                company.add(i[4])
        shop_totle_num = len(shop_totle)
        shop_active_num = len(shop_active)
        company_num = len(company)

        for sort in dict_sort:
            sort_list = dict_sort.get(sort)
            shop_set = {i[0]for i in sort_list}
            count_list = [float(i[1])if i[1] else 0 for i in sort_list]
            money_list = [float(i[2])if i[2] else 0 for i in sort_list]

            shop_num = len(shop_set)
            sales_count_num = sum(count_list)
            sales_money_num = sum(money_list)

            # print(platform,years,shop_totle_num,shop_active_num,company_num,sort,shop_num,sales_count_num,sales_money_num)
            print(platform, years, sort, shop_num, sales_count_num,sales_money_num)



        # for sort_zhejiang in dict_sort_zhejiang:
        #     sort_list = dict_sort_zhejiang.get(sort_zhejiang)
        #     shop_set = {i[0]for i in sort_list}
        #     count_list = [float(i[1])if i[1] else 0 for i in sort_list]
        #     money_list = [float(i[2])if i[2] else 0 for i in sort_list]
        #     shop_num = len(shop_set)
        #     sales_count_num = sum(count_list)
        #     sales_money_num = sum(money_list)
        #     print(platform,sort_zhejiang,shop_num,sales_count_num,sales_money_num,"zhejiang")

