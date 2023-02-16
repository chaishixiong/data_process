from collections import defaultdict
dict11 = defaultdict(list)
dict111 = {"tmall":0,"taobao_qiye":1,"jd":2,"a1688":3}
ww = open(r"C:\Users\Administrator\Desktop\jx1.csv","w",encoding="gbk")
with open(r"C:\Users\Administrator\Desktop\jx.txt","r",encoding="utf-8") as f:
    for i in f:
        data = i.strip().split(",")
        dict11[data[0]].append(data[1:])
with open(r"C:\Users\Administrator\Desktop\jx1.txt","r",encoding="utf-8") as f:
    for j in f:
        data1 = j.strip().split(",")
        company = data1[0]
        list1 = dict11.get(company,[])
        defut = [""]*120

        for list11 in list1:
            mouth = list11[0]
            pt = list11[1]
            value = list11[2]
            aa = 0
            if mouth.startswith("2019"):
                aa = 1
            elif mouth.startswith("2020"):
                aa = 2
            num = mouth[4:]
            num1 = dict111.get(pt)*30+aa*12+num-1
            defut[num1] = value
        str1 = j.strip()+","+",".join(defut)+"\n"
        ww.write(str1)