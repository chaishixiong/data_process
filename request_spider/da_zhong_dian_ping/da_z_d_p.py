import requests
import re
import pandas as pd
from lxml import etree
from request_spider.da_zhong_dian_ping.dzdp_settings import cate_list, css_dices


class DaZongDP(object):
    def __init__(self):
        self.css_url = None
        self.review_tag = None
        self.shop_num = None
        self.tag_name = None
        self.address = None
        self.cat_name = None
        self.next_url = [1]

    def request(self, url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xmlq=0.9,image/webp,image/apng,*/*q=0.8,application/signed-exchangev=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Cookie': 'navCtgScroll=100; _lxsdk=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; _lxsdk_cuid=1766018886cc8-04d7ab8077d427-5437971-4a574-1766020c6400; switchcityflashtoast=1; _hc.v=ce0d9b7c-277f-582f-7204-2d40c1c9a9cc.1614744421; s_ViewType=10; _tr.u=KmpIrpU4VFRQEB9E; _dp.ac.v=28882ee0-66fa-400f-a218-97da5a749b5b; ctu=2a2d9a661eb30bb6d36de26436e1fdf1857c55c22c0f2809953c81468300ca3a; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1619679169; source=m_browser_test_33; PHOENIX_ID=0a48873f-1791c776a08-610f; info="{\"query_id\":\"9dce19f9-c2a9-4884-99c4-0fe41c38b073\",\"ab_id\":\"exp000095_a\"}"; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3713187639; uamo=18779340395; cityid=106; fspop=test; pvhistory="6L+U5ZuePjo8L3F1emhvdS9jaCU3Qj46PDE2MjAzNzcxNDUyMTVdX1s="; m_flash2=1; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A11%7Cindex%3AA%3A3%7CshopList%3AA%3A5%7Cmap%3AA%3A1%7Cmyinfo%3AA%3A1; thirdtoken=e9214815-06a0-41d9-a0ef-2ed692fff555; _thirdu.c=35551c46e88dbc3a47a53c2e949b3cbd; aburl=1; Hm_lpvt_dbeeb675516927da776beeb1d9802bd4=1620875516; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1619681417,1619753965,1620379992,1620884253; cy=1; cye=shanghai; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1620963561; _lxsdk_s=17968eee122-354-86a-fc0%7C%7C68',
            'Host': 'www.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        }
        response = requests.get(url=url, headers=headers)
        return response

    def process_html(self, response):
        html = etree.HTML(response.text)
        ul_li = html.xpath('//*[@id="shop-all-list"]/ul/li')  # 多少个li标签
        number = len(ul_li)
        df = pd.DataFrame()
        self.next_url = html.xpath('//*[@class="next"]/@href')[0] if len(self.next_url) > 0 else None
        self.css_url = 'https:' + str(re.findall('//s3plus\.meituan\.net.+?\.css', (response.text))[0])
        for i in range(1, number + 1):
            # 详情url
            details_url = html.xpath("//li[{}]//div[@class='tit']/a[1]/@href".format(1))[0]
            # 标题
            title = html.xpath("//li[{}]//div[@class='tit']/a[1]/h4/text()".format(1))[0]
            # 评分
            score = html.xpath('//li[1]//div[@class="nebula_star"]/div[2]/text()'.format(i))[0]
            # 评论数
            comment_str = html.xpath('//li[{}]//a[@class="review-num"]/b//text()'.format(i))
            comment = self.str_data('shop_num', comment_str)
            # 人均价
            people_money_str = html.xpath(
                "//ul/li[{}]/div[@class='txt']/div[@class='comment']/a[@class='mean-price']/b//text()".format(i))
            people_money = self.str_data('shop_num', people_money_str)
            details_responts = self.request(details_url)
            category_name = self.category_name(details_responts)
            process_data = self.process_item(title, score, comment, people_money, category_name)
            data_mysql = self.data_warehousing(process_data)
        return df

    def category_name(self, details_responts):
        html = etree.HTML(details_responts.text)
        category_list = html.xpath('//div[@class="breadcrumb"]/a/text()')
        return category_list

    def css_data_dict(self, cat_num):
        url = "https://www.dianping.com/quzhou/ch{}".format(cat_num)
        responts = self.request(url)
        self.css_url = 'https:' + str(re.findall('//s3plus\.meituan\.net.+?\.css', (responts.text))[0])
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 's3plus.meituan.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        r = requests.get(self.css_url, headers=headers).content.decode()
        css_woff_list = re.findall(',url\("(.*?)"\);} ', r)
        data_list = []
        for url_s in css_woff_list:
            woff_url = 'https:' + url_s
            r = requests.get(woff_url, headers=headers).content
            from fontTools.ttLib import TTFont
            with open('responts.woff', 'wb')as f:
                f.write(r)
            addressfont = TTFont('responts.woff')
            addressfont.saveXML('responts.xml')
            address_TTGlyphs = addressfont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
            decrypt_data = {}
            address_dict = {}
            for i, x in enumerate(address_TTGlyphs):
                address_dict[x] = str(i)
            for k, v in zip(address_dict.keys(), css_dices.keys()):
                decrypt_data[k] = v
            data_list.append(decrypt_data)
        self.review_tag = data_list[0]
        self.shop_num = data_list[1]
        self.tag_name = data_list[2]
        self.address = data_list[3]

    def process_item(self, title, score, comment, people_money, category_name):
        item = dict()
        item['title'] = str(title).strip(' ')
        item['score'] = str(score)
        item['comment'] = comment
        item['price_text'] = people_money
        for i in range(0, len(category_name)):
            if i == 0:
                item['city_name'] = str(category_name[0]).strip(' ')
            elif i == 1:
                item['category_name'] = str(category_name[1]).strip(' ')
            elif i == 2:
                item['region_name'] = str(category_name[2]).strip(' ')
            elif i == 3:
                item['precise_name'] = str(category_name[3]).strip(' ')
        item['cat_name'] = self.cat_name
        return item

    def str_data(self, css_name, xpath_str):
        num_name = ''
        if css_name == 'shop_num':
            css_encryption = self.shop_num
        elif css_name == 'tag_name':
            css_encryption = self.tag_name
        elif css_name == 'address':
            css_encryption = self.address
        else:
            css_encryption = {}
        for i in range(0, len(xpath_str)):
            un_ue_str = str(xpath_str[i].encode('raw_unicode_escape').replace(b'\\', b''), 'utf-8')
            text = 'uni' + un_ue_str[1::1]
            if text in css_encryption.keys():
                num_name += css_encryption[text]
            else:
                num_name += str(xpath_str[i])
        return num_name

    def data_warehousing(self, process_data):
        with open('dazdp.txt', 'a', encoding='utf-8')as f:
            for item_str in process_data.values():
                f.write(item_str)
            f.write('\n')

    def run_begin(self, cat_num, cat_name):
        self.css_data_dict(cat_num + ',')
        while True:
            url = "https://www.dianping.com/quzhou/ch{}".format(cat_num)
            self.cat_name = cat_name
            responts = self.request(url)
            self.process_html(responts)
            if self.next_url == None:
                break


def run_d_z():
    run = DaZongDP()
    for cat_num, cat_name in zip(cate_list.keys(), cate_list.values()):
        run.run_begin(cat_num, cat_name)


if __name__ == '__main__':
    run_d_z()
