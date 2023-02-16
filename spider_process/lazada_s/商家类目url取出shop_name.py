import re
import os

def listdir(path,suffix,jiaoyan):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.splitext(file_path)[1] == suffix and jiaoyan in file:
            yield file_path

def file_process(file_path,new_file_path,host):
    with open(file_path, "r", encoding="utf-8") as f:
        shop_nameset = set()
        file_write = open(new_file_path,"w",encoding="utf-8")
        for i in f:
            shop_name = process_first(i)
            if shop_name not in shop_nameset and shop_name:
                url = "//www.lazada.{}/shop/{}/?langFlag=en&path=profile.htm&pageTypeId=3".format(host,shop_name)
                file_write.write(url+"\n")
                file_write.flush()
                shop_nameset.add(shop_name)
        file_write.close()

def process_first(file_str):
    shop_name = ""
    file_str = file_str.replace(r"\/", "/")
    if "/?" not in file_str:
        file_str = file_str.replace(r"?", "/?")
    match = re.search("/\?([^&=]+)&", file_str)
    if match:
        shop_name = match.group(1)
    else:
        match = re.search("/([^/]+)/\?", file_str)
        if match:
            shop_name = match.group(1)
        else:
            print("没有")
            print(file_str)
    return shop_name
if __name__=="__main__":
    path = r"X:\数据库\lazada采集"
    suffix = ".txt"
    jiaoyan = "lazada-合并"
    host = ""
    for i in listdir(path,suffix,jiaoyan):
        print("所选文件：",i)
        match = re.search("合并-([a-z\.]*)-",i)
        if match:
            host = match.group(1)
            new_file_path = path + r"\{{lazada-商家信息-{}-商家url}}[商家url].txt".format(host)
            print(host)
            print("新文件：",new_file_path)
            file_process(i,new_file_path,host)
            print("结束:", i)
        else:
            print("发生错误：host匹配错误")

