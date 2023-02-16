from tools.tools_s.sql_base import get_data
from collections import defaultdict
from unuse.data_count import main_dict_jd,main_dict_taobao
sql_prame = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
platforms = ["tmall"]
for platform in platforms:
    for years in [2018]:
        print(years)
        print(platform)
        if platform=="jd":
            main_dict = main_dict_jd
        else:
            main_dict = main_dict_taobao
        if years==2020:
            a= list(range(202001,202006))
        else:
            a= list(range(years*100+1,years*100+13))
        dict_sort = defaultdict(list)
        # dict_sort_zhejiang = defaultdict(list)
        shop_totle = set()
        shop_active = set()
        company = set()

        for year in a:
            # print(year)
            if platform=="jd":
                sql = "select main_sale,shop_id,sales_count*1 as sales_count,sales_money*1 as sales_money,company from {}_shopinfo_{} where city like'%温州%'".format(platform,year)
            elif platform=="taobao":
                sql = "select main_sale,shop_id,sales_count*1 as sales_count,sales_money*1 as sales_money,company from {}_shopinfo_{} where address like'%温州%'".format(platform,year)
            else:
                sql = "select main_sale,shop_id,sales_count*1 as sales_count,sales_money*1 as sales_money,company from {}_shopinfo_{} where city like'%温州%'".format(platform,year)

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
            print(platform,years,shop_totle_num,shop_active_num,company_num,sort,shop_num,sales_count_num,sales_money_num)
        # for sort_zhejiang in dict_sort_zhejiang:
        #     sort_list = dict_sort_zhejiang.get(sort_zhejiang)
        #     shop_set = {i[0]for i in sort_list}
        #     count_list = [float(i[1])if i[1] else 0 for i in sort_list]
        #     money_list = [float(i[2])if i[2] else 0 for i in sort_list]
        #     shop_num = len(shop_set)
        #     sales_count_num = sum(count_list)
        #     sales_money_num = sum(money_list)
        #     print(platform,sort_zhejiang,shop_num,sales_count_num,sales_money_num,"zhejiang")

