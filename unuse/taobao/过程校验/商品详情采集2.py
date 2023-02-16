import time

def get_danqian(platform):
    if platform == "taobao":
        totle_sale_count = 4416551
        totle_sale_money = 245154150000
        return int(totle_sale_count), int(totle_sale_money)
    else:
        totle_sale_count = 301515
        totle_sale_money = 315441560000
        return int(totle_sale_count), int(totle_sale_money)

def get_mouth(type,year=None,mouth=None):
    if not year or not mouth:
        a = time.localtime()
        b = a.tm_year
        c = a.tm_mon
    else:
        b = year
        c = mouth
    if type == 0:
        if c==1:
            c=12
            b=b-1
        elif c<11:
            c = "0"+str(c-1)
        return str(b) + str(c)
    elif type == 1:
        b = b - 1
        if c < 10:
            c = "0" + str(c)
        return str(b) + str(c)

def get_last(platform, mouth, type):
    path = r"X:/数据库/taobaotmall/过程校验/商品详情/"
    file_name = "{}销量统计结果.txt".format(platform)
    path_name = path + file_name
    youxiao = mouth + type

    with open(path_name, "r", encoding="utf-8") as f:
        for i in f:
            i = i.strip()
            if youxiao in i:
                data = i.split("：")[1]
                return int(float(data))

if __name__ == "__main__":
    platform = ["taobao", "tmall"]
    type_f = ["有效店铺","总销售额"]
    time_mouth = [0,1]
    year = 2019
    mouth = 7
    for type in time_mouth:
        mouth_now = get_mouth(type,year,mouth)
        for i in platform:
            now = get_danqian(i)
            for j in type_f:
                data = get_last(i, mouth_now, j)
                print("{}{}{}：{}".format(i,mouth_now,j,data))
                if data:
                    if j =="有效店铺":
                        bili = now[0]/data
                        print("{}{}{}现在：{}".format(i, mouth_now, j, now[0]))
                        print("{}{}{}比例：{}".format(i,mouth_now,j, bili))
                    else:
                        bili = now[1]/data
                        print("{}{}{}现在：{}".format(i, mouth_now, j, now[1]))
                        print("{}{}{}比例：{}".format(i,mouth_now,j, bili))