file = open(r"X:\数据库\taobao\{taobao_qiyeinfo_202012}[KEY,店铺名称,掌柜名称,开店时间,卖家信用,保证金,地区注册号,营业执照号,省,市,区].txt","w",encoding="utf-8")
with open(r"X:\数据库\taobao\{7_1_淘宝企业店铺_营业注册号}[KEY,店铺名称,掌柜名称,开店时间,卖家信用,保证金,地区注册号,营业执照号,省,市,区].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.split(",")
        if data[7].startswith("9"):
            file.write(i)
        else:
            data[6] = data[7][:6]
            i = ",".join(data)
            file.write(i)