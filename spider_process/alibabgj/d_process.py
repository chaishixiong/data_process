month = int(input("202012(除了1月1月要改):"))
last_month = month-1
sales_dict = dict()
with open(r"X:\数据库\阿里巴巴国际站\{xiaoliang}[key,name,sales_money,sales_num,company_type,keep_time].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        key = data[0]
        sales_money = data[2]
        sales_num = data[3]
        company_type = data[4]
        keep_time = data[5]
        sales_dict[key]=(sales_money,sales_num,company_type,keep_time)
zip_dict = dict()
with open(r"X:\数据库\阿里巴巴国际站\{地区邮编}[id,省,市,区].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        zip_id = data[0]
        province = data[1]
        city = data[2]
        county = data[3]
        zip_dict[zip_id]=(province,city,county)
file_write = open(r"X:\数据库\阿里巴巴国际站\{{alibabagj_shopinfo_{}}}[key,url,company_name,address_detail,country,province_e,city_e,address,zip,contact_people,sales_money,sales_num,company_type,keep_time,province,city,county].txt".format(month),"w",encoding="utf-8")
with open(r"X:\数据库\阿里巴巴国际站\{alibabagj_shopinfo}[key,url,company_name,address_detail,country,province,city,address,zip,contact_people,sales_money,sales_num,company_type,keep_time].txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        key = data[0]
        zip = data[8]
        sales = sales_dict.get(key,("","","",""))
        sales_money = sales[0]
        sales_num = sales[1]
        company_type = sales[2]
        keep_time = sales[3]
        zip_data = zip_dict.get(zip,("","",""))
        province = zip_data[0]
        city = zip_data[1]
        county = zip_data[2]
        data[-1]=keep_time
        data[-2]=company_type
        data[-3]=sales_num
        data[-4]=sales_money
        data.append(province)
        data.append(city)
        data.append(county)
        file_write.write(",".join(data)+"\n")
