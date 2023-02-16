dict_test = {}
a = '''VideoGames,Video Games
Video Games,Video Games
Toys&Games,Toys & Games
Toys & Games,Toys & Games
Tools&HomeImprovement,Tools & Home Improvement
Tools & Home Improvement,Tools & Home Improvement
Sports&Outdoors,Sports & Outdoors
Sports & Outdoors,Sports & Outdoors
PetSupplies,Pet Supplies
Pet Supplies,Pet Supplies
PatioLawn&Garden,Patio# Lawn & Garden
Patio，Lawn&Garden,Patio# Lawn & Garden
Patio， Lawn & Garden,Patio# Lawn & Garden
OfficeProducts,Office Products
Office Products,Office Products
MusicalInstruments,Musical Instruments
Musical Instruments,Musical Instruments
Industrial&Scientific,Industrial & Scientific
Industrial & Scientific,Industrial & Scientific
Home&Kitchen,Home & Kitchen
Home & Kitchen,Home & Kitchen
Health&Household,Health & Household
Health & Household,Health & Household
Grocery&GourmetFood,Grocery & Gourmet Food
Grocery & Gourmet Food,Grocery & Gourmet Food
Electronics,Electronics
ClothingShoes&Jewelry,Clothing# Shoes & Jewelry
Clothing，Shoes&Jewelry,Clothing# Shoes & Jewelry
Clothing， Shoes & Jewelry,Clothing# Shoes & Jewelry
CellPhones&Accessories,Cell Phones & Accessories
Cell Phones & Accessories,Cell Phones & Accessories
Beauty&PersonalCare,Beauty & Personal Care
Beauty & Personal Care,Beauty & Personal Care
BabyProducts,Baby Products
Baby Products,Baby Products
AutomotiveParts&Accessories,Automotive Parts & Accessories
Automotive Parts & Accessories,Automotive Parts & Accessories
ArtsCrafts&Sewing,Arts# Crafts & Sewing
Arts，Crafts&Sewing,Arts# Crafts & Sewing
Arts， Crafts & Sewing,Arts# Crafts & Sewing
Appliances,Appliances'''
f = a.split("\n")
for i in f:
    data = i.strip().split(",")
    dict_test[data[0]] = data[1]

def clears(str,dict):
    for i,y in dict.items():
        str = str.replace(i,y)
    return str


write_file = open(r"X:\数据库\美国亚马逊\202012\{3_3店铺分类_new}[id,main_sales,sort].txt","w",encoding="utf-8")
with open(r"X:\数据库\美国亚马逊\202012\{3_3店铺分类}[id,main_sales,sort].txt","r",encoding="utf-8") as f:
    for i in f:
        i_str = clears(i,dict_test)
        data_i = i_str.strip().split(",")
        data = data_i[2].split("，")
        new_data = []
        for i in data:
            if i not in new_data:
                new_data.append(i)
        data_i[2]="|".join(new_data)+"\n"
        new_str = ",".join(data_i)
        new_str= new_str.replace("#","，")
        write_file.write(new_str)

