import re
filer_name = r"O:/过程数据备份/淘宝天猫/201909/{10_1_淘宝上月月销大2商品ID}[网址].txt"
filew_name = r"O:/过程数据备份/淘宝天猫/201909/knalle_shopid.txt"
file = open(filew_name,"a+",encoding="utf-8")
with open(filer_name,"r",encoding="utf-8") as f:
    num = 1
    for i in f:
        try:
            match_shopid = re.search("seller_id=(.*?)&",i)
            if match_shopid:
                shop_id = match_shopid.group(1)
                file.write(shop_id+"\n")
            else:
                print("meiyou")
            if num % 200000 == 0:
                print(num)
                file.flush()
        except Exception as e:
            print(e)