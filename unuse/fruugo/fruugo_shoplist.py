file = open(r"W:\scrapy_xc\fruugo_sort-data_seed.txt","w",encoding="utf-8")
def get_pagenum(num,page):
    if num%page:
        page_num = int(num/page)+1
    else:
        page_num = int(num/page)
    return page_num

with open(r"W:\scrapy_xc\fruugo_sort-data_合并.txt_去重.txt[F1,F5,F6].txt","r",encoding="utf-8") as f:
    totle_num = 0
    for i in f:
        data = i.strip().split(",")
        num = get_pagenum(int(data[1]), 64)
        limitnum = 1000
        if num > limitnum:
            num = limitnum
        totle_num += num
        for i in range(1,num+1):
            url = data[0]+"?page={},{}\n".format(i,data[2])
            file.write(url)
    print(totle_num)