import requests
import redis

import json
import jsonpath
import time
import random
def headers_todict(header_str):
    header = header_str.split("\n")
    headers = {}
    for cookie in header:
        if ":" in cookie:
            cookie_split = cookie.split(":",1)
            name = cookie_split[0].strip()
            values = cookie_split[1].strip()
            headers[name] = values
        else:
            headers[cookie] = ""
    return headers
class DianPingSpider():
    cate_dict = {10: "美食", 25: "电影演出赛事", 30: "休闲娱乐", 60: "酒店", 50: "丽人", 15: "K歌", 45: "运动健身", 35: "周边游", 70: "亲子",
                 55: "结婚", 20: "购物", 95: "宠物", 80: "生活服务", 75: "学习培训", 65: "爱车", 85: "医疗健康", 90: "家居", 40: "宴会"}
    city_dict = {106: "衢州", 888: "江山市", 889: "常山县", 890: "开化县", 891: "龙游县", 878: "桐乡市"}
    city_dict1 = {106: "quzhou", 888: "jianshan", 889: "changshan", 890: "kaihua", 891: "liuyou", 878: "tongxiang"}

    def __init__(self):
        self.key = "dianping_seed"
        self.key_cache = "dianping_seed_cache"

        self.server = redis.Redis(host="192.168.0.225", port=5208,decode_responses=True)
        self.file = open("./dianping_data.txt","a",encoding="utf-8")

    def seed_push(self):
        for city_num in self.city_dict.keys():
            for cate_num in self.cate_dict.keys():
                #处理种子
                page = "1"
                self.server.lpush(self.key, "{}-{}-{}".format(city_num, cate_num, page))
    def run(self):
        self.cookies = input("cookies:")
        self.token = input("token:")
        self.process()

    def process(self):
        # while True:
        while True:
            a = self.server.rpoplpush(self.key_cache, self.key)
            if not a:
                break
        while True:
            key = self.server.rpoplpush(self.key,self.key_cache)
            if not key:
                break
            result,next_seed = self.request_process(key)
            if result:
                self.server.lrem(self.key_cache,key,0)
                if next_seed:
                    self.server.lpush(self.key,next_seed)
            else:
                break
            time.sleep(random.random() * 5 + 8)
        self.file.close()

    def request_process(self,key):
        url = "http://m.dianping.com/isoapi/module"
        headers = self.get_header()
        parameter = self.get_parameter()
        data = key.split("-")
        area = int(data[0])
        type = int(data[1])
        page = int(data[2])
        area_pinyin = self.city_dict1.get(area)
        headers["Referer"] = "https://m.dianping.com/{}/ch{}".format(area_pinyin,type)
        headers["Cookie"] = parameter.get("Cookie")
        tiken = parameter.get("token")
        data = '''{{"pageEnName":"shopList","moduleInfoList":[{{"moduleName":"mapiSearch","query":{{"search":{{"start":{},"categoryId":"{}","parentCategoryId":{},"locateCityid":0,"limit":20,"sortId":"0","cityId":{},"regionId":0,"maptype":0,"keyword":""}}}}}}],"_token":"{}"}}'''.format(
            (page-1)*20,type,type,area,tiken
        )
        try:
            req = requests.post(url,data=data,headers=headers)
            judge = '"success"'
        except Exception as e:
            judge = ''
        if judge and judge in req.text:
            #解析
            #将结果
            isEnd = ""
            try:
                json_data = json.loads(req.text)
                listData = jsonpath.jsonpath(json_data, "$..listData")
                cate_id = jsonpath.jsonpath(json_data, "$..categoryId")
                isEnd1 = jsonpath.jsonpath(json_data, "$..isEnd")
                if isEnd1:
                    isEnd = isEnd1[0]
                if cate_id:
                    cate_id = cate_id[0]
                    cate_name = self.cate_dict.get(int(cate_id), "")
                else:
                    cate_name = ""
                city_id = jsonpath.jsonpath(json_data, "$..cityId")
                if city_id:
                    city_id = city_id[0]
                    city_name = self.city_dict.get(int(city_id), "")
                else:
                    city_name = ""
                if listData:
                    list = listData[0].get("list")
                    recordCount = listData[0].get("recordCount")
                    for i in list:
                        shop_id = i.get("shopuuid","")
                        shop_name = i.get("name","")
                        branchName = i.get("branchName","")
                        starScore = str(i.get("starScore",""))
                        reviewCount = str(i.get("reviewCount",""))
                        priceText = i.get("priceText","")
                        regionName = i.get("regionName","")
                        categoryName = i.get("categoryName","")
                        dishtags = i.get("dishtags", "")
                        dishtags = dishtags.replace(",", "，")
                        hasTakeaway = str(i.get("hasTakeaway",""))
                        self.file.write(",".join(
                            [str(recordCount), shop_id, shop_name, branchName, starScore, reviewCount, priceText,
                             regionName,categoryName, dishtags, hasTakeaway, city_name, cate_name]) + "\n")
                self.file.flush()
            except Exception as e:
                print("解析发生错误：{}".format(key),e)
            if isEnd and page < 50:
                return 1,"{}-{}-{}".format(area,type,page+1)
            else:
                return 1,0
        else:#cookies失效
            return 0,0


    def get_parameter(self):
        result = {"Cookie":self.cookies,"token":self.token}
        return result

    def get_header(self):
        header = '''Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Type: application/json
Host: m.dianping.com
Origin: https://m.dianping.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'''
        return headers_todict(header)


if __name__=="__main__":
    a = DianPingSpider()
    # a.seed_push()
    a.run()