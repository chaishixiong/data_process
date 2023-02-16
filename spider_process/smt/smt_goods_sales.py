from tqdm import tqdm
def get_comment_bili(file_name):
    totle_comment_num = 0
    mouth_comment_num = 0
    with open(file_name,"r",encoding="utf-8") as f:
        for i in f.readlines():
            data = i.strip().split(",")
            totle_comment_num+=int(data[5]) if data[5] else 0
            mouth_comment_num+=int(data[7]) if data[7] else 0
    return totle_comment_num,mouth_comment_num
# area = input("字母地区:")
# area_d = {"other":"其他","zhejiang":"浙江"}
# area_z = area_d.get(area)
mouth = input("202201:")

file_write = open("X:\数据库\速卖通\{{smt_monthsales_{}}}[店铺id,卖家id,商品id,销量,商品价格,评论数量,新评论数量,当月评论数,计算比例,当月销量].txt".format(mouth),"w",encoding="utf-8")
file_name = "X:\数据库\速卖通\{{速卖通_商品}}[店铺id,卖家id,商品id,销量,商品价格,评论数量,新评论数量,当月评论数].txt".format()
totle_comment_num,mouth_comment_num = get_comment_bili(file_name)
totle_bili = mouth_comment_num/totle_comment_num#计算总体评论当月比例
print("总体比例：{}".format(totle_bili))
zhengtai = 0.5
with open(file_name, "r", encoding="utf-8") as f:
    for i in tqdm(f.readlines()):
        data = i.strip().split(",")
        try:
            price = float(data[4]) if data[4] else 0  #  商品价格
            sales_num = int(data[3]) if data[3] else 0  #  销量
            comment_numlod = int(data[5]) if data[5] else 0  #  评论数量
            comment_numnew = int(data[6]) if data[6] else 0  #  新评论数量
            comment_num = comment_numnew if comment_numnew else comment_numlod  #
            comment_mouth = int(data[7]) if data[7] else 0  #  当月评论数
            if sales_num:
                if comment_num:
                    sales_bili = comment_mouth/comment_num
                    if sales_bili < (totle_bili*zhengtai) and sales_num > comment_num:
                        sales_bili = sales_bili*comment_num/sales_num+(totle_bili*zhengtai)*(sales_num-comment_num)/sales_num
                    if sales_bili > 1:
                        sales_bili = 1
                else:
                    sales_bili = totle_bili#使用整理比例
                sales_money = sales_bili*sales_num*price
            else:
                sales_bili = 0
                sales_money = 0
            # print(sales_num,price,comment_num,comment_numnew,comment_mouth,sales_bili,sales_money)
            file_write.write(i.strip()+",{:.2f},{:.2f}\n".format(sales_bili,sales_money))
        except Exception as e:
            print(i, e)
