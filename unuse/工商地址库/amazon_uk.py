#将公司名称分割成5000为单位的多个文本
from pathlib import Path
import os
import time
import xlsxwriter

def creat_work(fw_name):
    workbook = xlsxwriter.Workbook(fw_name)
    work_sheel = workbook.add_worksheet("sheel1")
    work_sheel.write(0,0,"批量查询")
    work_sheel.write(1,0,'''注意事项
    1. 模版中的表头名称不可更改，表头行不可删除；
    2. 第一行内容为实例，可以修改或删除；
    3. 企业名称要与工商登记的名称一致；
    4.单次查询企业最多5000家，单次查询信用报告和受益人最多200家。''')
    work_sheel.write(2,0,"企业名称")
    return workbook,work_sheel
path = "X:\数据库\工商地址库"
mouth = time.localtime().tm_mon
type = input("last_now:")
if "now" in type:
    qichacha_mouth = Path(path) / (str(7)+"_add")
else:
    qichacha_mouth = Path(path)/str(mouth)
if not os.path.exists(qichacha_mouth):
    os.mkdir(qichacha_mouth)

#数据处理
# 一上月，last：读取：{company_last}[company].txt
company_file = "{{company_{}}}[company].txt".format(type)

# 二新增，now：读取：{company_now_add}[company].txt
# company_file = "{{company_{}_add}}[company].txt".format(type)

qichacha_file = Path(path)/company_file
file_num = 1
fw_name = qichacha_mouth/"gmnriat{}.xlsx".format(file_num*5000)
workbook,work_sheel = creat_work(fw_name)
with open(qichacha_file,'r',encoding="utf-8") as f:
    num = 0
    for data in f:
        if num <5000:
            pass
        else:
            file_num+=1
            num=0
            workbook.close()
            fw_name = qichacha_mouth / "gmnriat{}.xlsx".format(file_num * 5000)
            workbook, work_sheel = creat_work(fw_name)
        company = data.strip()
        #这里传企查查数据可以处理下
        row = 3+num
        col = 0
        work_sheel.write(row,col,company)
        num += 1
    workbook.close()

