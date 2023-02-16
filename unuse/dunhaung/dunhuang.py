file_w = open(r"O:\采集数据备份\敦煌\202001\文本文件\{敦煌_业务信息_dui}[店铺ID,公司名称,统一社会信用代码,法人代表,经营范围,成立时间,营业期限至,登记机关,登记状态,地址,省,市,区].txt","w",encoding="utf-8")
with open(r"O:\采集数据备份\敦煌\202001\文本文件\{敦煌_业务信息}[店铺ID,公司名称,统一社会信用代码,法人代表,经营范围,成立时间,营业期限至,登记机关,登记状态].txt","r",encoding="utf-8") as f:
    num = 0
    for i in f:
        data = i.strip().split(",")
        data.extend([""]*4)
        try:
            data[0]= data[0].replace("sale-items/","")
            data[0]= data[0].replace(".html","")
            int(data[0])
            if len(data) == 13:
                file_w.write(",".join(data)+"\n")
                pass
            else:
                print(1)
                # num+=1
                # print(i)
                # if len(data)>13:
                #     data = data[:13]
                # else:
                #     num = len(data)
                #     data.extend([""]*(13-num))
                # file_w.write(",".join(data)+"\n")
        except Exception as e:
            num+=1
            print(i,e)
    print(num)

