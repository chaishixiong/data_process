from tools.tools_s.sql_base import get_data
from collections import defaultdict
seller_set = set()
# zhejiang_set = set()
# with open(r"X:\数据库\taobao\{tmall_shopid_zhejiang}[shop_id,seller_id].txt","r",encoding="utf-8") as f:
#     for i in f:
#         seler = i.strip().split(",")[1]
#         zhejiang_set.add(seler)
with open(r"X:\数据库\taobao\{5_2_4_asyn店铺详情_浙江淘宝_new}[标识,店铺ID,卖家ID,公司名称,描述,服务,物流,卖家用户名].txt","r",encoding="utf-8") as f:
    for i in f:
        seler = i.strip().split(",")[2]
        seller_set.add(seler)
sql_prame = {
    "host": "192.168.0.227",
    "db": "oridata_taobao",
    "port": 9227,
    "user": "read",
    "password": "nriat227read@x#"
}

class MaxJudge():
    result = defaultdict(list)
    def __init__(self,seller_set):
        self.seller_set = seller_set
        # self.zhejiang_set = zhejiang_set

    def judge(self,goods_id,seller_id,sales_month):
        if seller_id in self.seller_set:
            data = self.result.get(seller_id,[])
            if len(data)<3 or sales_month > 10 :#and seller_id in self.zhejiang_set
                self.result[seller_id].append((goods_id,seller_id,sales_month))

    def get_result(self):
        return self.result

sql = "select goods_id,seller_id,sales_month from taobao_goodsmobile_202102"
datas = get_data(sql_prame,sql)


file_w = open(r"X:\数据库\taobao\taobaoyilou_seed.txt","w",encoding="utf-8")
mg = MaxJudge(seller_set)#zhejiang_set
for data in datas:
    sales = data[2]
    if not data[2]:
        sales = 0
    mg.judge(data[0],data[1],int(sales))
result = mg.get_result()
for i in result.values():
    for j in i:
        file_w.write("{},{}\n".format(j[0],j[1]))