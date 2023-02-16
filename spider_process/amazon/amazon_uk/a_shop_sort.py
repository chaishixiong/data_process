from collections import defaultdict
import os
#需要X:\数据库\美国亚马逊\（上月）中的 3_3店铺分类文件
#需要 amazon_sortshop文件

month = int(input("202012(除了1月1月要改):"))
last_month = 202212
shop_dict = defaultdict(list)
write_file_all = open("X:\数据库\欧洲亚马逊\{3_3店铺分类}[id,main_sales,sort].txt", "w", encoding="utf-8")
shop_set = set()
if os.path.exists("X:\数据库\欧洲亚马逊\{{amazon_uk_sortshop-data_{}}}[url,id,name,num,sort].txt".format(month)):
    write_file = open("X:\数据库\欧洲亚马逊\{{3_3店铺分类_{}}}[id,main_sales,sort].txt".format(month), "w", encoding="utf-8")
    with open("X:\数据库\欧洲亚马逊\{{amazon_uk_sortshop-data_{}}}[url,id,name,num,sort].txt".format(month), "r",encoding="utf-8",errors="ignore") as f:
        for i in f:
            try:
                data = i.strip().split(",")
                shop_id = data[1]
                comment_num = data[3]
                comment_num = comment_num.replace("，", "")
                if comment_num:
                    comment_num = int(comment_num)
                sort = data[4]
                shop_dict[shop_id].append((comment_num, sort))
            except:
                print(i)
    for i, j in shop_dict.items():
        shop_id = i
        if shop_id not in shop_set:
            shop_set.add(shop_id)
            shop_sort = sorted(j, key=lambda x: x[0], reverse=True)
            main_sales = shop_sort[0][1]
            sort_list = []
            for sort in shop_sort:
                if sort[1] not in sort_list:
                    sort_list.append(sort[1])
            write_file.write("{},{},{}\n".format(shop_id, main_sales, "|".join(sort_list)))
            write_file_all.write("{},{},{}\n".format(shop_id, main_sales, "|".join(sort_list)))
with open("X:\数据库\欧洲亚马逊\{}\{{3_3店铺分类}}[id,main_sales,sort].txt".format(last_month), "r", encoding="utf-8") as f:
    for i in f:
        shop_id = i.split(",")[0]
        if shop_id not in shop_set:
            shop_set.add(shop_id)
            write_file_all.write(i)


