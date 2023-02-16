#
import os
import re
class file_process():
    def get_data(self,file_name,num=1,data_num=1):
        with open(file_name,"r",encoding="utf-8") as f:
            if num ==1:
                for i in f:
                    i = i.strip()
                    yield i
            else:
                for i in f:
                    i_list = i.split(",")
                    i = i_list[data_num-1]
                    i = i.strip()
                    yield i
    def listdir(self,path,str):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if re.search(str,file_path) and "python" not in file_path:
                yield file_path
if __name__ == "__main__":

    path = r"X:\数据库\lazada采集"
    a = input("是否为更新店铺表的操作（是或否）:")#要输入
    if a=="是":
        str_need = "{lazada_shopinfo_[a-z]*?}"         #2222---对最后一步店铺表操作   ：：是
    else:
        str_need = "lazada-商家类目url"                 #1111---对商家类目url操作   ：：否
    file_process = file_process()
    file_list = file_process.listdir(path,str_need)
    for i in file_list:
        print(i)
        if a =="是":
            write_filename = i.replace("lazada_shopinfo","lazada_shopinfo_python")
        else:
            write_filename = i.replace(str_need,str_need+"_python")
        file = open(write_filename,"w",encoding="utf-8")
        datalist = file_process.get_data(i)
        for j in datalist:
            j = j.replace(r"锛?","，")
            j = j.replace(r"\/","/")
            j = j.replace(r"?","/?")
            j = re.sub("，.*?&","&",j)
            file.write(j+"\n")
        file.close()
    data = file_process.get_data("")


