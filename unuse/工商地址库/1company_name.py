from tools.tools_s.sql_base import get_data
from pathlib import Path
from tools.tools_d.tools_process import tools_file

mouth = int(input("本月爬取月份（如202005）:"))
# ==================上月处理
pts_dict ={"tmall":"oridata_tmall","taobao":"oridata_taobao","jd":"oridata_jd","suning":"oridata_ec_other","gome":"oridata_ec_other"}
pts = ["tmall","jd","taobao_qiye","suning","gome"]
#

# =================本月处理
# pts_dict ={"tmall":"oridata_tmall","jd":"oridata_jd","suning":"oridata_ec_other","gome":"oridata_ec_other"}
# pts = ["tmall","jd","suning","gome"]

sql_prame = {
    "host": "192.168.0.228",
    "db": "e_commerce",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
sql_prame_227 = {
    "host": "192.168.0.227",
    "db": "",
    "user": "dev",
    "password": "Data227or8Dev715#"
}
company_set = set()
path = "X:\数据库\工商地址库"
file_name = "{{company_{}}}[company].txt".format(input('last_or_now:'))
write_path = Path(path)/file_name
file_write = open(write_path,"w",encoding="utf-8")
for pt in pts:
    if "last" in file_name:
        for i in [mouth-2,mouth-1]:#年份再改
            sql = '''select distinct(company) from {}_shopinfo_{}'''.format(pt,i)
            company_data = get_data(sql_prame,sql)
            for data in company_data:
                if data[0] not in company_set:
                    file_write.write(data[0]+"\n")
                    company_set.add(data[0])
    else:
        if pt =="taobao_qiye":
            pt = "taobao"
        sql_prame_227['db']=pts_dict.get(pt)
        sql = '''select distinct(company) from {}_shopinfo_{}'''.format(pt, mouth)
        company_data = get_data(sql_prame_227, sql)
        for data in company_data:
            if data[0] not in company_set:
                file_write.write(data[0] + "\n")
                company_set.add(data[0])
    print("{}好".format(pt))
else:
    if "now" in file_name:
        file_write.close()
        file_namew = file_name.replace("}", "_add}")
        old_file = file_name.replace("now","last")
        data_tool = tools_file()
        data_tool.two_data_p(path, file_name, old_file, file_namew, dict_name="setdiff1d")


