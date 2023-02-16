# # -*- coding:utf-8 -*-
#
# # 导入pandas包并重命名为pd
# import pandas as pd
# '''20210408-161905gmarket_spidershopinfo124_合并.txt'''
# # 读取Excel中Sheet1中的数据，并且导出
# data = pd.DataFrame(pd.read_csv('W:\scrapy_xc\gmarket_spider-data\A20210408-161905gmarket_spider124_合并.txt', chunksize=100000))
# # 查看读取数据内容
# print("读取记录：%s条" % len(data))
# repeat_flag = data.duplicated(subset='Column10',keep=False)
#
# # print(repeat_flag)
# no_rep_data=data[repeat_flag==False]
# rep_data=data[repeat_flag==True]
# print("重复记录：%s条"%len(rep_data))
# rep_data_sort = rep_data.sort_values(axis=0,ascending=True,by=["Column2"])
# rep_data_rst=rep_data_sort.drop_duplicates(subset='Column10',keep='first')
# result=pd.concat([no_rep_data,rep_data_rst],axis=0)
# print("输出记录：%s条"%len(result))
# result.to_excel('./excel/output.xlsx',index=False)
import time
import pandas as pd
# chunksize = 10000
# s = time.time()
# df = pd.DataFrame()
# num = 0
# for chunk in pd.read_csv('W:\scrapy_xc\gmarket_spider-data\A20210408-161905gmarket_spider124_合并.txt', chunksize=chunksize):
#     df = pd.concat([df, chunk])
#     df.drop_duplicates(subset=['507372168'], keep='first', inplace=True)
#     df.to_csv('W:\scrapy_xc\gmarket_spider-data\A20210408-161905gmarket_spider124_quchong.txt', sep=',', header=True,
#               index=None)
#     # print(df)
#     num += 10000
#     print(num)
# print('读取耗时', time.time() - s)
# print('去重前', df.shape[0])
# s = time.time()
# print('去重耗时', time.time()-s)
# print('去重后', df.shape[0])
# print('---------------------------------------------------')
import requests


class CsEbay(object):
    def __init__(self):
        pass

    def request(self, us_name):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        url = 'https://www.ebay.com/sch/{}/m.html?_nkw&_armrs=1&_from&rt=nc&LH_PrefLoc=6'.format(us_name)
        # hedaers = {
        #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
        # }
        cookie_str = '__gads=ID=9bc276b1fedc8d26:T=1614061756:S=ALNI_MYvtCBnG-TUZ8DcTnmuX7hI9bQAGA; JSESSIONID=8ECD3508A8F3F96E804B813AC7D90CDA; ds2=; ns1=BAQAAAXguCEiyAAaAANgATGJmVM5jNzJ8NjAxXjE2MTU1MTI1MDk4MTZeXjFeM3wyfDV8NHw3fDExXjFeMl40XjNeMTJeMTJeMl4xXjFeMF4xXjBeMV42NDQyNDU5MDc1wch7nLOGrIFNV1uhLox8juDjmX4*; s=CgADuAGBghnLNMwZodHRwczovL3d3dy5lYmF5LmNvbS9zY2gvc3l6YXFzeS9tLmh0bWw/X25rdyZfYXJtcnM9MSZfZnJvbSZydD1uYyZMSF9QcmVmTG9jPTYjaXRlbTRkYmI3MGNjMTgHAPgAIGCGcs0yZmNiZjU2ODE3MjBhYWVjYmI2NWM5NDNmZjhkNzQwNHUswGI*; npii=btguid/2fcbf5681720aaecbb65c943ff8d74046447884e^cguid/2fcbfdec1720a6e5b576ccd7d3b85a946447884e^; nonsession=CgAAIABxgrK5OMTYxOTMzNjIxMHgzMzM4NTcyMTM0NjR4MHgyWQDKACBkR4hOMmZjYmY1NjgxNzIwYWFlY2JiNjVjOTQzZmY4ZDc0MDQAywACYIUoVjM22ACDVA**; ebay=%5Ejs%3D1%5Esbf%3D%2341c00000000010000100000%5Epsi%3DA1ObM%2FLY*%5E; dp1=bu1p/QEBfX0BAX19AQA**6447884e^pbf/#e000e0000001000200000064487e62^tzo/-1e064478856^bl/CN6447884e^'
        cookie_dict = {i.split('=')[0]: i.split('=')[1] for i in cookie_str.split(';')}
        r = requests.get(url, hedaers=headers, cookies=cookie_dict)
        r_html = r.text()
        print(r_html)

    def print_shop_num(self):
        pass

    def open_txt(self):
        with open(r'W:/scrapy_seed/ebayinfo_goods.txt') as f:
            ebay_text = f.readlines()
            for i in ebay_text:
                us_name = i.strip()
                self.request(us_name)
                print(us_name)
            f.close()
        pass

def run_cs_ebay():
    run_cs = CsEbay()
    run_cs.open_txt()

if __name__ == '__main__':
    run_cs_ebay()
