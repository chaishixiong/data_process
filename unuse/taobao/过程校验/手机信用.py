import os

def set_return(file_name):
    shop_id_set =set()
    with open(file_name,"r",encoding="utf-8") as f_r:
        num1 = 1
        for i in f_r.readlines():
            if num1 % 1000000 == 0:
                print(num1)
            num1 += 1
            str_list = i.strip().split(",")
            shop_id = str_list[0]
            shop_id_set.add(shop_id)
    return shop_id_set
def file_write(filename,path,w_file,zhongdian_file):
    name = "手机店铺信用"
    file = w_file
    filename_zhe = path+filename
    filename_yue = path+"上月/"+filename
    filename_nian = path+"上年/"+filename
    filename_zhongdian = path+"重点/"+filename

    zhe_set = set_return(filename_zhe)
    yue_set = set_return(filename_yue)
    nian_set = set_return(filename_nian)
    zhongdian_set = set_return(filename_zhongdian)

    huanbi = round(len(zhe_set)/len(yue_set),6)
    h_add = len(zhe_set-yue_set)
    h_lost = len(yue_set-zhe_set)

    tongbi = round(len(zhe_set)/len(nian_set),6)
    t_add = len(zhe_set-nian_set)
    t_lost = len(nian_set-zhe_set)

    z_lost = len(zhongdian_set-zhe_set)
    for i in zhongdian_set-zhe_set:
        zhongdian_file.write(i+"\n")
    z_bili = round(z_lost/len(zhongdian_set),6)

    file.write("{}这月：".format(name)+str(len(zhe_set))+"\n")
    file.write("{}上月：".format(name)+str(len(yue_set))+"\n")
    file.write("{}上年：".format(name)+str(len(nian_set))+"\n")
    file.write("{}上月重点商铺：".format(name)+str(len(zhongdian_set))+"\n")
    file.write("{}环比数量：".format(name)+str(huanbi)+"\n")
    file.write("{}较上月增量：".format(name)+str(h_add)+"\n")
    file.write("{}较上月减少：".format(name)+str(h_lost)+"\n")
    file.write("{}同比数量：".format(name)+str(tongbi)+"\n")
    file.write("{}较上年增量：".format(name)+str(t_add)+"\n")
    file.write("{}较上年减少：".format(name)+str(t_lost)+"\n")
    file.write("{}重点商铺这个月少得：".format(name)+str(z_lost)+"\n")
    file.write("{}重点商铺比例：".format(name)+str(z_bili)+"\n")
    file.write("\n")

if __name__ == "__main__":
    path = r"X:/数据库/taobaotmall/过程校验/手机店铺信用/"
    w_file = path+"信用统计结果.txt"
    zhongdian_file = path+"重点店铺较上月减少seller_id.txt"

    w_file = open(w_file,"a+",encoding="utf-8")
    zhongdian_file = open(zhongdian_file,"a+",encoding="utf-8")

    for file in os.listdir(path):
        if file.endswith(".txt") and "3_1_淘宝天猫卖家ID" in file:
            file_write(file,path,w_file,zhongdian_file)
    w_file.close()



