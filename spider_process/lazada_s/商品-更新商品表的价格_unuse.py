import re
import os
from pathlib import PureWindowsPath,Path

def listdir(path,suffix,jiaoyan):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        match = re.search(jiaoyan,file_path)
        if match and os.path.splitext(file_path)[1] == suffix :
            yield file_path,match.group(1)
def process(data,r1,r2):
    data_list = data.strip().split(",")
    if len(data_list) == 18:
        data_list[3] = data_list[3].replace(r1, "")
        data_list[4] = data_list[4].replace(r1, "")
        data_list[3] = data_list[3].replace(r2, "")
        data_list[4] = data_list[4].replace(r2, "")
        num_d1 = data_list[3].count(".")
        if num_d1 > 1:
            data_list[3] = data_list[3].replace(".", "", num_d1 - 1)
        num_d2 = data_list[4].count(".")
        if num_d2 > 1:
            data_list[4] = data_list[4].replace(".", "", num_d2 - 1)
        try:
            if data_list[3]:
                float(data_list[3])
            if data_list[3]:
                float(data_list[4])
        except:
            print(data_list)
    else:
        print(data_list)
    return data_list
if __name__=="__main__":
    path = r"X:\数据库\lazada采集"
    suffix = ".txt"
    jiaoyan = "lazada_goodsinfo_(.*?)}"
    # lazada_platerm_dict = {
    #     "coid":"Rp",
    #     "coth":"฿",
    #     "commy": "RM",
    #     "comph": "₱",
    #     "sg": "$",
    #     "vn": " ₫",
    # }
    for i in listdir(path, suffix, jiaoyan):
        path_name = Path(path)
        file_seeds = path_name/"{{lazada_goodsinfo_python_{}}}[KEY,商品名称,商品id,原来价格,现在价格,评论分数,评论数量,评论分布,品牌,品牌url,商家名称,商家id,商家url,商家积极的卖家评级,商家准时发货,商家聊天回复率,商品highlights,平台].txt".format(i[1])
        print(file_seeds)
        w_file = open(file_seeds,"a",encoding="utf-8")
        # r1 = lazada_platerm_dict.get(i[1])
        r2 = "，"
        with open(i[0],"r",encoding="utf-8") as f:
            num_j = 0
            for j in f:
                num_j += 1
                if num_j % 100000 == 0:
                    print(num_j)
                data = process(j,"",r2)
                # data.append("lazada"+i[1])
                w_file.write(",".join(data)+"\n")
        w_file.close()