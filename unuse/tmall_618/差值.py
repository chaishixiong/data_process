
file1 = r"X:\数据库\618\sales\不包含\{taobao_sales高}[goods_id,sales_max].txt"
file2 = r"X:\数据库\618\sales\不包含\{tmall_goodsmobile_618_1_all}[商品ID,月销量].txt"
filew = r"X:\数据库\618\sales\不包含\{taobao_sales_1}[goods_id,sales_min,sales_max,sales_cha].txt"

dict_seed = dict()
fiel_w = open(filew,"w",encoding="utf-8")
with open(file1,"r",encoding="utf-8") as f:#最大值
    for i in f:
        data = i.strip().split(",")
        dict_seed[data[0]] = data[1]
with open(file2,"r",encoding="utf-8") as f1:#17号的
    for j in f1:
        data1 = j.strip().split(",")
        id= data1[0]
        max = dict_seed.get(data1[0])
        if max:
            max1 = int(max)
        else:
            max1 = 0
        min = data1[1]
        if min:
            min1 = int(min)
        else:
            min1 = 0
        cha = max1-min1
        if cha < 0:
            cha =0
        fiel_w.write("{},{},{},{}\n".format(id,min1,max1,cha))