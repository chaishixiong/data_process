import re

import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

response = requests.get('https://www.gmarket.co.kr/', headers=headers)

tree = etree.HTML(response.text)
urls = tree.xpath('//li[contains(@class, "list-item__2depth")]/a/@href')
f = open(r'./cat_url1.txt', 'w', encoding='utf-8')
for url in urls:
    response1 = requests.get(url=url, headers=headers)
    tree1 = etree.HTML(response1.text)
    urlss = tree1.xpath('//div[@id="divMiddleLayer"]/div/ul/li/a/@href')
    for i in urlss:
        if re.findall(r'category', i):
            urll = i.split(',')[1].replace('"', '').replace("'", '') + '&v=l'
            f.write(urll + '\n')