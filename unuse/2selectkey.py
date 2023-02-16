import re
from pathlib import Path

def commend6():
    mouth = input("输入月份(202005):")
    path = r"X:\数据库\阿里巴巴国际站"
    file_named = "{{alibabagj_shopid_{}}}[供应商名称,供应商url,供应商6个月销售额,供应商6个月销量,供应商历史总销售额,供应商历史总销量,供应商提供年数,供应商出口主要国家,供应商的贸易保证限额,供应商的交易等级,供应商回复时间,供应商回复率,供应商国家,供应商省,供应商产品url,评论分数,评论数,评论url].txt".format(mouth)
    file = Path(path)/file_named
    file_namew = "{alibabagj_shopid_id}[key].txt"
    file_namew1 = "{alibabagj_shopid}[key,供应商名称,供应商url,供应商6个月销售额,供应商6个月销量,供应商历史总销售额,供应商历史总销量,供应商提供年数,供应商出口主要国家,供应商的贸易保证限额,供应商的交易等级,供应商回复时间,供应商回复率,供应商国家,供应商省,供应商产品url,评论分数,评论数,评论url].txt"
    file_w = open(Path(path)/file_namew,"w",encoding="utf-8")
    file_w1 = open(Path(path)/file_namew1,"w",encoding="utf-8")
    match_s = "//(.*?)\.alibaba\.com|member/(.*?)/"
    with open(file,"r",encoding="utf-8") as f:
        for i in f:
            data = i.strip().split(",")
            url = data[1]
            url_s = url.replace(r"\/","/")
            match = re.search(match_s,url_s)
            if match:
                key = match.group(1)
                file_w.write(key+"\n")
                file_w1.write(key+","+i)
            else:
                print(i)
commend6()