import re
def url_to_m(url):
    judge = re.match("https://[^\.]+\.m\.tmall",url)
    if judge:
        return url
    else:
        tmall_key_match = re.match("//([^\.]+)\.?m?\.tmall", url)
        if tmall_key_match:
            new_url = "https://{}.m.tmall".format(tmall_key_match.group(1))
            return new_url
        else:
            print(url)
            return ""
if __name__ == "__main__":
    f_w = open(r"X:\数据库\taobao\{3_1_天猫卖家ID}[KEY,卖家ID,url天猫,飞猪]new.txt","w",encoding="utf-8")
    with open(r"X:\数据库\taobao\{3_1_天猫卖家ID}[KEY,卖家ID,url天猫,飞猪] - 副本.txt_去重.txt","r",encoding="utf-8") as f:
        num = 0
        for i in f:
            num+=1
            if not num%10000:
                print(num)
            data = i.strip().split(",")
            url = data[2]
            new_url = url_to_m(url)
            data[2] = new_url
            f_w.write(",".join(data)+"\n")

