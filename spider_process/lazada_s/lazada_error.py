import re
file = "Y:\自动化任务\(20200707-191929)采集_lazada-商家信息_取接口url_vn\自动任务27001-27501.txt"
file1 = r"Y:\自动化任务\(20200707-191929)采集_lazada-商家信息_取接口url_vn\1自动任务27001-27501.txt"

file_w =  open(file1,"w",encoding="utf-8")

with open(file,"r",encoding="utf-8") as f:
    for i in f:
        match = re.search("/shop/[a-zA-Z0-9\-]+/\?",i)
        if match:
            file_w.write(i)
        else:
            print(i)
