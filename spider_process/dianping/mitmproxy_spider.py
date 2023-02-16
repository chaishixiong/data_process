from mitmproxy.http import flow
import json
import jsonpath
cate_dict = {10: "美食", 25: "电影演出赛事", 30: "休闲娱乐", 60: "酒店", 50: "丽人", 15: "K歌", 45: "运动健身", 35: "周边游", 70: "亲子",
 55: "结婚", 20: "购物", 95: "宠物", 80: "生活服务", 75: "学习培训", 65: "爱车", 85: "医疗健康", 90: "家居", 40: "宴会"}

city_dict = {106:"衢州",888:"江山市",889:"常山县",890:"开化县",891:"龙游县",878:"桐乡市"}
file = open("./dianping_data.txt","a",encoding="utf-8")
def request(flow:flow):
    pass

def response(flow:flow):
    if "isoapi" in flow.request.url:
        json_data = json.loads(flow.response.text)
        listData = jsonpath.jsonpath(json_data, "$..listData")
        cate_id = jsonpath.jsonpath(json_data, "$..categoryId")
        if cate_id:
            cate_id = cate_id[0]
            cate_name = cate_dict.get(int(cate_id),"")
        else:
            cate_name = ""
        city_id = jsonpath.jsonpath(json_data, "$..cityId")
        if city_id:
            city_id = city_id[0]
            city_name = city_dict.get(int(city_id),"")
        else:
            city_name = ""
        if listData:
            list = listData[0].get("list")
            recordCount = listData[0].get("recordCount")
            for i in list:
                shop_id = i.get("shopuuid")
                shop_name = i.get("name")
                branchName = i.get("branchName")
                starScore = str(i.get("starScore"))
                reviewCount = str(i.get("reviewCount"))
                priceText = i.get("priceText")
                regionName = i.get("regionName")
                categoryName = i.get("categoryName")
                dishtags = i.get("dishtags","")
                dishtags = dishtags.replace(",","，")
                hasTakeaway = str(i.get("hasTakeaway"))
                file.write(",".join([str(recordCount),shop_id,shop_name,branchName,starScore,reviewCount,priceText,regionName,categoryName,dishtags,hasTakeaway,city_name,cate_name])+"\n")
    
    #mitmdump -q -s mitmproxy_spider.py -p 8080

