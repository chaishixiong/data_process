# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# import js2py
# import os
# import re
# import time
# import threading
# import execjs
# import requests
# import json
# import redis
# import socket,re
# mutex = threading.Lock()
#
#
# def get_ip():
#     addrs = socket.getaddrinfo(socket.gethostname(), "")
#     match = re.search("'192.168.(\d+.\d+)'", str(addrs))
#     ip_num = "0.000"
#     if match:
#         ip_num = match.group(1)
#     return ip_num
#
# def if_ip():
#     if get_ip() in ["9.10","9.11","9.42","9.127","9.128","10.101","10.102","10.103","10.104","10.105","10.106","10.100","9.97","9.95","9.122","9.68","9.100"]:
#         USER_NAME = "057762355592"
#         PASSWORD = "928858"
#     elif get_ip() == "9.123":
#         USER_NAME = "wzlcb57746616"
#         PASSWORD = "123456"
#     elif get_ip() == "9.124":
#         USER_NAME = "wzlcf57746616"
#         PASSWORD = "123456"
#     elif get_ip() == "9.125":
#         USER_NAME = "wzlcg57746616"
#         PASSWORD = "123456"
#     elif get_ip() == "9.126":
#         USER_NAME = "wzlcc57746616"
#         PASSWORD = "123456"
#     elif get_ip() in ["9.148","9.149","9.170","9.171","9.172","9.173","9.182"]:
#         USER_NAME = "057764473605"
#         PASSWORD = "744523"
#     else:
#         USER_NAME = "057762355594"#9.100 9.99 9.98 0.56 0.59 9.129
#         PASSWORD = "045805"
#     if get_ip() == "0.226" or get_ip() == "7.144":
#         USER_NAME = "null"
#         PASSWORD = "null"
#     return USER_NAME, PASSWORD
#
# '''<class 'dict'>: {'_m_h5_tk': '3183ad262c286ca290f39883b94b2c95_1623924818882', '_m_h5_tk_enc': 'b6099178d60d7688fde0e3b8694b2e88'}'''
# class TbTM618(object):
#     def __init__(self):
#         with open(r"W:\scrapy_chai\run_tm_618\taobao_sgin.js", encoding='utf-8') as f:
#             self.cx = f.read()
#         self.cookie = 'WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuCTNvlJkGJJJFSIzUzDgsGKQKMYyNwg%3D; _w_app_lg=0; t=25ba3f5de30e5119e5cb46f844c666e6; lgc=%5Cu4E09%5Cu9014%5Cu6CB3%5Cu8FD8%5Cu662F%5Cu5929%5Cu5802; tracknick=%5Cu4E09%5Cu9014%5Cu6CB3%5Cu8FD8%5Cu662F%5Cu5929%5Cu5802; thw=cn; enc=y%2FNLzo3clbGPY4p1YcsJ35ziFXKcaUiqdB5AqZZR0eNo9CdMQw%2BDPt92I6lnPlXY%2FVetyxnP%2Ble5PMVvKtPj%2FA%3D%3D; miid=1892902211012796874; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zMG1aAN%2F0SGVHunXe1zncjzZgd4rdD%2FjILQOrtuN9AcrFGtraBZ1RodkLNw253fwy23xcP1Nurzqg%2FMACx%2FMt%2BXwAKoWSimfE3zBY9eqAXSnImqxfbKNs6CDAY%2FORuOtVhUU6SSLTq0mGo%2BljTuwSuBUxtaZvfrPLrtZu2D0zAaRoSbFYq2sZU4p1V5peDg8b0RlK%2FlcUfjT2nydE8v8G%2Bd%2FKgV8aSnMZgM2APAQCRm4MoiuC3C%2Ftfltp1s9gmYYkHCHobvC%2FgGPnBh%2Fb5rgcpQskxmZzMcd02VHKOmRJIy34G9xDjvJQsnDO5w9kYg7J%2BRldiXpON%2FoY4mQ%3D%3D; _samesite_flag_=true; cookie2=16763a4eef778f510db0b6112af6b384; dnk=%5Cu4E09%5Cu9014%5Cu6CB3%5Cu8FD8%5Cu662F%5Cu5929%5Cu5802; hng=CN%7Czh-CN%7CCNY%7C156; v=0; existShop=MTYyMzAzMjIzNA%3D%3D; linezing_session=PKjcCOnBP2OSTDS6pPjGKmbX_1623051099040nM7W_15; _tb_token_=f1be73b333e39; cna=Oy1GGbUaUFMCAX14XODD4pDh; ockeqeudmj=p4I8Dmg%3D; sgcookie=E100ywv3s5ovIMtY7jrjzB%2BbFpXzftdnXoBEqmnHdPBtCAevEufuS2xhZyMWro1B%2Fo8gNhXWfaCZme8aQNM3Pogi2g%3D%3D; uc3=id2=UonfNi0%2FFrMiHg%3D%3D&nk2=q6SExg6ViDH5dsxxo5k%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dCuw7%2FHrqxuFA8kuY%3D; csg=dcdb60cc; skt=c149ca5aff23778a; uc4=id4=0%40UOE1hWxiCMmVsrMn8EuMYcWF5jDr&nk4=0%40qRFYgdeR9m4Y%2B9Q9PN9eVz%2FidJXzaV5CEw%3D%3D; _cc_=U%2BGCWk%2F7og%3D%3D; mt=ci=-1_0; xlly_s=1; _m_h5_tk={}; _m_h5_tk_enc={}; tfstk=ct8PBAZR743zUUbIXa_UOMlKm05Ra08HzrWPqnO6ywyu2JslQs24pscbpsWVBqjl.; l=eBgB_l6gjKHVGVhoBO5wKurza77tBIOf1sPzaNbMiInca1ld1p21eNCB6sDpRdtjgt5fLetr2SGpXdEe8f4_WE90MWpDRs5mpw9wRe1..; uc1=cookie14=Uoe2zs7efpdDAA%3D%3D; isg=BDIyaRg5hoTGj7r0HzDPEeBXg3gUwzZdMaLBRvwLzeXQj9KJ5FKJbVmufysz_671'
#         self.data = '{"detail_v":"3.5.0","exParams":"{\"appReqFrom\":\"detail\",\"container_type\":\"xdetail\",\"dinamic_v3\":\"true\",\"supportV7\":\"true\",\"ultron2\":\"true\"}","itemNumId":"%s","pageCode":"miniAppDetail","_from_":"miniapp"}'
#         self._m_h5_tk_first = 'undefined'
#         self.url = 'https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.6.1&appKey=12574478&t={}&sign={}&api=mtop.taobao.detail.getdetail&v=6.0&ttid=202012%40taobao_h5_9.17.0&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp1&data=%7B%22detail_v%22%3A%223.5.0%22%2C%22exParams%22%3A%22%7B%5C%22appReqFrom%5C%22%3A%5C%22detail%5C%22%2C%5C%22container_type%5C%22%3A%5C%22xdetail%5C%22%2C%5C%22dinamic_v3%5C%22%3A%5C%22true%5C%22%2C%5C%22supportV7%5C%22%3A%5C%22true%5C%22%2C%5C%22ultron2%5C%22%3A%5C%22true%5C%22%7D%22%2C%22itemNumId%22%3A%22{}%22%2C%22pageCode%22%3A%22miniAppDetail%22%2C%22_from_%22%3A%22miniapp%22%7D'
#         self.time_dd = ''
#         self.username, self.password = if_ip()
#         self.redisPool = redis.Redis(host='192.168.0.225', port=5208, db=0, decode_responses=True)
#         self.error_key = "tm_618_goods:error_url"
#
#     def get_sign(self, data):
#         ctx = execjs.compile(self.cx)
#         self.time_dd = str(int(time.time() * 1000))
#         sign_str = self._m_h5_tk_first + "&" + self.time_dd + "&" + "12574478" + "&" + data
#         sign = ctx.call("get_sign_demo", sign_str)
#         return sign
#
#     def request(self, sign, goods_id):
#         url = self.url.format(self.time_dd, sign, goods_id)
#         headers = {
#             "accept": "*/*",
#             "accept-language": "zh-CN,zh;q=0.9",
#             "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
#             "sec-ch-ua-mobile": "?0",
#             "sec-fetch-dest": "script",
#             "sec-fetch-mode": "no-cors",
#             "sec-fetch-site": "same-site",
#             "authority": "h5api.m.taobao.com",
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
#             "referer": "https://h5.m.taobao.com/",
#             "cookie": "cna=Dew6FmbpdV8CAX1tYcc5BefV; enc=R%2FiIADstSBcS55mu5oYZ4%2FB4H34KkfwEDv%2B%2Bd5lSYzgs0ZeOwdz34OyB%2FhPIUTrMATrTkGv6UrjZx%2FQhtfEp3A%3D%3D; tg=0; sgcookie=EMuT2y4dvngNgbO8b%2Fi4m; miid=209769241100503190; _samesite_flag_=true; cookie2=1094c282f95576413cfa79f40e54e0e5; t=59b7d7633d87aabc35c981dcb81a27aa; _tb_token_=7355e34e7573d; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5v1WA9tqDMGe6T2Zngm5goVZnJIueGXYupDskPApt9SL58KvTW5K05TTwaY%2BItz3bdIju9twreBbdqB3Vu5wbJokepQJV4KQuY%2BpmGrb7fvq8RQlu5d1Ah8z3wboA988lPwf1NJ5%2BqwIu6Fifd%2FxCTV%2FahV47p%2F4MQMHomVMhuvl1tMd9oGBDEf3SMTY%2FqB59HjMK55M%2FISQX2retITPJaXsB8pTnqqrDwQzgjMESR2WvzIJXWLSvqlM2I%3D; linezing_session=6TcYaShsNg4DGiqHV4sM6p0V_16237422581223PzP_1; xlly_s=1; tfstk=cvR5BOMMxuq7dTMUaUg4LJTf_6CCZPNfJY_9Pd2zzxQzpi85ihPNfg1HKkVABZ1..; l=eBTWlwkqONp9Hiq2BOfwourza77OSIRAguPzaNbMiOCP_A1p5OJVW6OGMrL9C3GVh6xMR3u-CtXWBeYBqIqE8gK21b-GL9kmn; isg=BAIC-SEq1hYGJfUXqDiuXD5YUwhk0wbt8fp6k0wbJXUgn6IZNGPp_YCeT5vjz36F"
#         }
#         time.sleep(2)
#         r = requests.get(url=url, headers=headers)
#         return r
#
#     def connect(self):
#         name = "宽带连接"
#         username = self.username
#         password = self.password
#         cmd_str = "rasdial %s %s %s" % (name, username, password)
#         res = os.system(cmd_str)
#         if res == 0:
#             print("连接成功")
#             return "成功"
#         else:
#             print("连接失败")
#             return "失败"
#
#     def disconnect(self):
#         name = "宽带连接"
#         cmdstr = "rasdial %s /disconnect" % name
#         os.system(cmdstr)
#         print('断开成功')
#
#     def huan_ip(self):
#         # 断开网络
#         self.disconnect()
#         # 开始拨号
#         a = self.connect()
#         return a
#
#     def process_item(self, respones):
#         item = dict()
#         match = re.search("mtopjsonp1\((.*)\)", respones.text)
#         json_str = match.group(1)
#         json_data = json.loads(json_str)
#         mark_1 = re.search("(满200减30)", json_str)
#         mark_2 = re.search("(满199减20)", json_str)
#         mark_3 = re.search("(跨店)", json_str)
#         if mark_1 is not None:
#             mark = mark_1.group(1)
#         elif mark_2 is not None:
#             mark = mark_2.group(1)
#         else:
#             mark = ''
#         if mark_3 is not None:
#             mark2 = '跨店'
#         else:
#             mark2 = ''
#         item['goods_id'] = json_data['data']['item']['itemId']
#         item['mark'] = mark
#         item['mark2'] = mark2
#         with open('W:\scrapy_xc\{taobao_618_logo}.txt', 'a', encoding='utf-8')as f:
#             for i in item.values():
#                 f.write(i + ',')
#             f.write('\n')
#         return item
#
#     def redis_list(self):
#         goods_id = self.redisPool.spop('tm_618_goods:request_goods')
#         return goods_id
#
#     def cookies_generate(self, goodid):
#         url = "https://h5api.m.taobao.com/h5/mtop.taobao.baichuan.smb.get/1.0/?jsv=2.6.1&appKey={}&t={}&sign={}&api=mtop.taobao.baichuan.smb.get&v=1.0&type=originaljson&dataType=jsonp&timeout=10000"
#         time_now = str(int(time.time() * 1000))
#         appkey = "12574478"
#         data = '{}'
#         sign = self.get_sign(data)
#         url = url.format(appkey, time_now, sign)
#         data1 = {"pageCode":"mainDetail","ua":"Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36 Edg/86.0.622.48","params":"{\"url\":\"https://h5.m.taobao.com/awp/core/detail.htm?id=%s\",\"referrer\":\"\",\"oneId\":null,\"isTBInstalled\":\"null\",\"fid\":\"dSnxbHpDSQi\"}" % goodid}
#         headers = {'Host': 'h5api.m.taobao.com', 'Connection': 'keep-alive',
#                    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Mobile Safari/537.36 Edg/86.0.622.48',
#                    'Accept': '*/*', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'no-cors',
#                    'Sec-Fetch-Dest': 'script', 'Referer': 'https://h5.m.taobao.com/',
#                    'Accept-Encoding': 'gzip, deflate, br',
#                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
#         try:
#             req = requests.post(url=url, headers=headers, data=data1)
#             headers_rep = req.headers
#             set_cookiesstr = headers_rep.get("set-cookie")
#             set_cookies = self.reqhead_split(set_cookiesstr)
#             cookies_dict = dict()
#             cookies_dict["_m_h5_tk"] = set_cookies.get("_m_h5_tk", "")
#             cookies_dict["_m_h5_tk_enc"] = set_cookies.get("_m_h5_tk_enc", "")
#             if cookies_dict.get("_m_h5_tk") and cookies_dict.get("_m_h5_tk_enc"):
#                 return cookies_dict
#         except Exception as e:
#             print(e)
#             pass
#
#     def reqhead_split(self, headers_str):
#         b = re.sub("(expires=[^,]*),", "\\1，", headers_str, flags=re.I)
#         h_list = b.split(",")
#         dict_p = {}
#         for str_p in h_list:
#             parameter = str_p.split(";")[0]
#             parameter_l = parameter.split("=", 1)
#             value_p = ""
#             if len(parameter_l) > 1:
#                 value_p = parameter_l[1].strip()
#             name_p = parameter_l[0].strip()
#             dict_p[name_p] = value_p
#         return dict_p
#
#     def run_tb(self):
#         while True:
#             goods_id = self.redis_list()
#             data = self.data % goods_id
#             sign = self.get_sign(data)
#             respones = self.request(sign, goods_id)
#             data_str = respones.content.decode()
#             try:
#                 data_dict = self.process_item(respones)
#                 print(data_dict)
#             except Exception as e:
#                 if "被挤爆" in data_str:
#                     time.sleep(10)
#                     # cookies_dict = self.cookies_generate(goods_id)
#                     # self.cookie = self.cookie.format(cookies_dict['_m_h5_tk'], cookies_dict['_m_h5_tk_enc'])
#                     print(data_str)
#                 else:
#                     # state = self.huan_ip()
#                     # cookies_dict = self.cookies_generate(goods_id)
#                     # self.cookie = self.cookie.format(cookies_dict['_m_h5_tk'], cookies_dict['_m_h5_tk_enc'])
#                     time.sleep(10)
#                 self.redisPool.lpush(self.error_key, goods_id)
#
# def open_goods():
#     import redis
#     with open(r"W:\scrapy_xc\taobao_618_look-data_ll\good_seet.txt", "r",encoding="utf-8") as f:
#         goods_str = f.read()
#         f.close()
#     redisPool = redis.ConnectionPool(host='192.168.0.225', port=5208, db=0, decode_responses=True)
#     redis = redis.Redis(connection_pool=redisPool)
#     good_list = goods_str.split('\n')
#     for goods in good_list:
#         redis.sadd('tm_618_goods:request_goods', goods)
#
#
#
#
# def withopen():
#     r = TbTM618()
#     r.run_tb()
#
#
# if __name__ == "__main__":
#     _m_h5_tk_first = 'undefined'
#     time_dd = str(int(time.time() * 1000))
#     data = '{"detail_v":"3.5.0","exParams":"{\"appReqFrom\":\"detail\",\"container_type\":\"xdetail\",\"dinamic_v3\":\"true\",\"supportV7\":\"true\",\"ultron2\":\"true\"}","itemNumId":"643349031200","pageCode":"miniAppDetail","_from_":"miniapp"}'
#     withopen()
#     # open_goods()

# =====================================================================================================
# =====================================================================================================
# =====================================================================================================

shop_dict = {}
# month = int(input("202012(除了1月1月要改):"))
# last_month = 1 if month == 12 else month-1
with open(r"X:\数据库\taobao\\{3_4_天猫卖家ID}[KEY,卖家ID].txt", "r", encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        shop_id = data[0]
        seller_id = data[1]
        shop_dict[seller_id] = shop_id

# bid_dict = {}
# with open(r"X:\数据库\taobao\{8_0_0_天猫商品信息}[商品ID,库存,bid].txt", "r", encoding="utf-8") as f:
#     num = 0
#     for i in f:
#         num += 1
#         if num % 1000000 == 0:
#             print(num)
#         data = i.strip().split(",")
#         goods_id = data[0]
#         inventory_id = data[1]
#         bid = data[2]
#         bid_dict[goods_id] = (inventory_id, bid)
#
# b_name = {}
# with open(r"X:\数据库\taobao\bid_bname.csv", "r", encoding="utf-8") as f_f:
#     b_num = 0
#     for i_i in f_f:
#         b_num += 1
#         if b_num % 1000000 == 0:
#             print(b_num)
#         data = i_i.strip().split(",")
#         b_name_id = data[0]
#         name_b = data[1]
#         b_name[b_name_id] = name_b

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# mark_name = {}
# pric_data = {}
# with open(r"X:\数据库\taobao\{taobao_618_look-5}.txt", "r", encoding="utf-8") as ma_ma:
#     m_num = 0
#     for m_m in ma_ma:
#         m_num += 1
#         if m_num % 1000000 == 0:
#             print(m_num)
#         try:
#             data_5 = m_m.strip().split(",")
#             sales_month = data_5[3]
#             goods_id = data_5[1]
#             mark_name[goods_id] = sales_month
#             pric_data[goods_id] = data_5[15]
#         except Exception as e:
#             print(e)
# bid_name = {}
# cid_name = {}
# with open(r"X:\数据库\taobao\{618_cat}[cid,bid,c_name1,c_name2].txt", "r", encoding="utf-8") as cid_cid:
#     c_num = 0
#     for c_c in cid_cid:
#         c_num += 1
#         if c_num % 1000000 == 0:
#             print(c_num)
#         try:
#             cid_data = c_c.strip().split(",")
#             cid_id = cid_data[0]
#             bid_id = cid_data[1]
#             cid_name[cid_id] =  cid_data[2]
#             bid_name[bid_id] = cid_data[3]
#         except Exception as e:
#             print(e)
#
# f_1_dact = {}
# with open(r"X:\数据库\taobao\{{tmall_goodsmobile_1_202106}}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性].txt","r",encoding="utf-8") as f_1:
#     f_num_1 = 0
#     for c_c in f_1:
#         f_num_1 += 1
#         if f_num_1 % 1000000 == 0:
#             print(f_num_1)
#         try:
#             cid_data = c_c.strip().split(",")
#             f_1_good_id = cid_data[1]
#             f_1_dact[f_1_good_id] = cid_data[3]
#         except Exception as e:
#             print(e)
#
#
#
# file_write = open(r"X:\数据库\taobao\tmall_goodsmobile_618_202102.txt", "w", encoding="utf-8")
# with open(r"X:\数据库\taobao\{{tmall_goodsmobile_2_202106}}[采集时间,商品ID,近似销量,月销量,评论数,总库存,收藏量,发货地址,类目ID,品牌ID,平台,商品名称,卖家ID,店铺ID,促销名称,促销价,定金,定金描述,原价名称,原价,配送费用,商品保证,网店推广,推广描述,商品积分,主图,商品属性].txt","r",encoding="utf-8") as f:
#     b_type = "B"
#     num = 0
#     for i in f:
#         num += 1
#         data = i.strip().split(",")
#         goodsid = data[1]
#         xiao_l = mark_name.get(goodsid) # 5月份数据
#         xiao_2 = f_1_dact.get(goodsid)  # 第一轮数据
#         jia_ge = pric_data.get(goodsid) # 5月份价格
#         if xiao_l == None:
#             xiao_ling = '0'
#         else:
#             xiao_ling = mark_name.get(goodsid)
#         if jia_ge == None:
#             jiage = '0'
#         else:
#             jiage = pric_data.get(goodsid)
#         if len(data[3]) < 0:
#             xiao_ling_1 = '0'
#         else:
#             xiao_ling_1 = data[3]
#         if len(data[14]) < 0:
#             jiage_1 = '0'
#         else:
#             jiage_1 = data[14]
#         if xiao_2 == None:
#             f_1_xiaoliang = '0'
#         else:
#             f_1_xiaoliang = f_1_dact.get(goodsid)
#         sales_cha = int(xiao_ling_1) - int(xiao_ling)
#         if sales_cha > 0:
#             data[25] = str(sales_cha)
#             sales_money = str(float(jiage_1) * sales_cha)
#         else:
#             data[25] = '0'
#             sales_money = '0'
#         sales_cha_2 = int(xiao_ling_1) - int(f_1_xiaoliang)
#         data[26] = sales_money
#         cid_c = data[8]
#         bid_bb = data[9]
#         cid_nnmm = cid_name.get(cid_c)
#         bid_nnmm = bid_name.get(bid_bb)
#         if cid_nnmm != None:
#             data[22] = cid_nnmm
#         else:
#             data[22] = ''
#         if bid_nnmm != None:
#             data[23] = bid_nnmm
#         else:
#             data[23] = ''
#         if sales_cha_2 > 0:
#             sales_cha_ = (str(sales_cha_2))
#             sales_money2 = (str(float(jiage_1) * sales_cha_2))
#             data.append(sales_cha_)
#             data.append(sales_money2)
#         else:
#             data.append('0')
#             data.append('0')
#         file_write.write(",".join(data)+"\n")
#         if num % 1000000 == 0:
#             print(num)
#             file_write.flush()
        # except Exception as e:
        #     print(e)

# class DataDict(object):
#     def __init__(self):
#         pass
#
#     def dict_dict(self):
#         mark_2_name = {}
#         with open(r"X:\数据库\taobao\taobao_618_2_look-data.txt", "r", encoding="utf-8") as ma_ma:
#             num_2 = 0
#             for m_m in ma_ma:
#                 num_2 += 1
#                 if num_2 % 1000000 == 0:
#                     print(num_2)
#                 try:
#                     data_2 = m_m.strip().split(",")
#                     b_name_id = data_2[0]
#                     b_s_2 = data_2[8]
#                     mark_2_name[b_name_id] = b_s_2
#                 except Exception as e:
#                     print(e)
#         return mark_2_name
#
#     def updata_dict(self, data_2):
#         with open(r"X:\数据库\taobao\taobao_618_2_look-data.txt", "r", encoding="utf-8") as ma_ma:
#             b_type = "B"
#             num = 0
#             for i in ma_ma:
#                 try:
#                     num += 1
#                     write_data = [""] * 27
#                     write_data[1] = goods_id  # goods_id 商品ID
#                     write_data[2] = sales_mouth  # veges_month 销量
#                     write_data[3] = sales_mouth  # sales_month 销量
#                     write_data[4] = ''  # comment_count
#                     write_data[5] = inventory  # inventory
#                     write_data[6] = ''  # collect_num
#                     write_data[7] = ''  # address 发货地址
#                     write_data[8] = cid  # cid 天猫类目ID
#                     write_data[9] = bid  # bid 天猫品牌ID
#                     write_data[10] = b_type  # bc_type 平台
#                     write_data[11] = good_name  # goods_name 天猫商品名称
#                     write_data[12] = seller_id  # seller_id 卖家ID
#                     write_data[13] = shop_id  # shop_id 店铺ID
#                     write_data[14] = price  # discount_price 折扣价
#                     write_data[15] = price  # real_price 真实扣价
#                     write_data[16] = ''  # price_area 区间价格
#                     write_data[17] = ''  # price
#                     write_data[18] = pic  # image_url
#                     write_data[19] = mark  # mark 双十一标识
#                     write_data[20] = ''  # mark2 跨店
#                     write_data[21] = ''  # obtained 是否下架
#                     write_data[22] = ''  # c_name1 类别
#                     write_data[23] = ''  # c_name2 类别2
#                     write_data[24] = bb_name  # b_name 品牌name
#                     write_data[25] = ''  # sales_cha 销量差值
#                     write_data[26] = ''  # sales_money 销售额
#                     file_write.write(",".join(write_data)+"\n")
#                     if num % 1000000 == 0:
#                         print(num)
#                         file_write.flush()
#                 except Exception as e:
#                     print(e)
#     def run_dict(self):
#         data_1, data_2 = self.dict_dict()
#         self.updata_dict(data_1, data_2)
eb_dict = {}
with open(r"W:\scrapy_xc\ebayinfo_goods-data.txt", "r", encoding="utf-8") as cid_cid:
    c_num = 0
    for c_c in cid_cid:
        c_num += 1
        if c_num % 1000000 == 0:
            print(c_num)
        try:
            cid_data = c_c.strip().split(",")
            ebay_name = cid_data[0]
            ebay_id = cid_data[1]
            eb_dict[ebay_name] =  ebay_id
        except Exception as e:
            print(e)