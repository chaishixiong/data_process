import re
def process(str_input):
    str_input = str_input.replace("http:","https:")
    str_input = str_input.replace("-/-","-")
    if "catalog" not in str_input:
        str_input = str_input.replace("com/","com/catalog/")
    str_input = str_input.replace("pid","cid")
    str_input = re.sub(r"([^g])/(\w{4,6}-)",r"\1-\2",str_input)
    return str_input
file = open("X:\数据库\阿里巴巴国际站\{1_阿里巴巴国际站-导航页-分类url}[key].txt","w",encoding="utf-8")
with open("X:\数据库\阿里巴巴国际站\{1_阿里巴巴国际站-导航页-分类url}[分类url].txt","r",encoding="utf-8") as f:
    for i in f:
        i = process(i)
        file.write(i)