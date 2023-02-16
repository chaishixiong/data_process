#数字校验
import pymysql
from collections import defaultdict

host = "192.168.0.227"
port = 3306
db = "ec_cross_border"
name = "dev"
password = "Data227or8Dev715#"

amazon = {"columns":["ratings","reviews"],"table":"amazonus_goodsinfo_201908_copy1"}#"Price",
dh = {"columns":["comment","minPrice","maxPrice","Orders"],"table":"dhgate_goodsinfo_201907_copy1"}
ebay = {"columns":["price_dollar","price_RMB","sales_count"],"table":"ebay_goodsinfo_201907_copy1"}
lazada = {"columns":["price_lod","price_now","ratings","reviews"],"table":"lazadacoid_goodsinfo_201909_copy1"}
alibabgj = {"columns":["price","price_low","ratings","reviews","sales_num"],"table":"alibabagj_goodsinfo_201908_copy1"}
smt = {"columns":["minPrice","maxPrice","sales_num"],"table":"smt_goodsinfo_201904_copy1"}

softtime = {"columns":["CommentCount","Score","CurrentSalePrice","SalePrice","SaleCount","ActualSalePrice","Volume"],"table":"softtime_goodsinfo_201908_copy1"}
file = open(r"C:\Users\admin\Desktop\error.txt","a+",encoding="utf-8")
dict_p = softtime
def get_data(connect,sql_select):
    cursor = connect.cursor()
    num = cursor.execute(sql_select)
    print(num)
    headers = cursor.description
    data = cursor.fetchall()#匹配表里的data
    return data,num,headers
connect1 = pymysql.connect(host=host,port=port,db=db,user=name,passwd=password,charset="utf8",use_unicode=True,cursorclass=pymysql.cursors.Cursor)

columns = dict_p.get("columns")
columns_str = ",".join(columns)
sql_select = '''select {} from {}'''.format((columns_str),dict_p.get("table"))
file.write("这个是{}表的数字错误记录\n".format(dict_p.get("table")))


data,num,headers = get_data(connect1,sql_select)
connect1.close()
data_dict = defaultdict(list)
print_num = 0
for one_data in data:
    if print_num % 1000 == 0:
        print(print_num)
    print_num += 1
    try:
        for c_data in one_data:
            if c_data:
                float(c_data)
    except Exception as e:
        print(e)
        file.write(str(one_data)+"\n")


