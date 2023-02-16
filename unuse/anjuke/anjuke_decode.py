import io
import re
from fontTools.ttLib import TTFont
import base64

def get_dict(base64_str):
    ttf = base64.decodebytes(base64_str.encode())
    font = TTFont(io.BytesIO(ttf))
    a = font.getBestCmap()  # 获取cmap的映射关系
    #
    id_dict = dict()
    for i, y in a.items():
        # print(str(hex(i)),y)
        y = int(re.sub("\D", "", y))
        id_dict[str(hex(i))] = str(y-1)
        print(str(hex(i)), y)
    return id_dict
if __name__=="__main__":
    base64_dict = dict()
    write_file = open(r"X:\数据库\安居客\{ods_renthouse_original}[ID,城市,楼层,户型,出租类型,面积,朝向,价格,房源概况,base64].txt","w",encoding="utf-8")
    with open(r"X:\数据库\安居客\{租房_原始}[ID,城市,楼层,户型,出租类型,面积,朝向,价格,房源概况,base64].txt","r",encoding="utf-8") as f:
        for txt_data in f:
            txt_data = re.sub("&#x([\da-fA-F]{4});","0x\\1",txt_data)
            # print(txt_data)
            data = txt_data.strip().split(",")
            base64_str = data[9]
            if base64_str:
                if base64_str not in base64_dict:
                    base64_dict[base64_str] = get_dict(base64_str)
                css_map = base64_dict.get(base64_str)
                # print(css_map)
                for map_i,map_y in css_map.items():
                    txt_data = txt_data.replace(map_i,map_y)
                write_file.write(txt_data)
