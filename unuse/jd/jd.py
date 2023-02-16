from tqdm import tqdm

save_path = 'X:/数据库/002-京东2-第三方/'
path = 'X:/数据库/002-京东2-第三方/{2_1_京东第三方商品表_入库}[店铺ID,商品ID,主图,商品名称,CID,CID1,CID2,评论数,价格,好评率].txt'
goods_dic = {}
with open(path, 'r', encoding='utf-8') as f:
    for i in tqdm(f):
        info = []
        goodinfo = i.replace('\n', '').split(',')
        PID = goodinfo[1]
        good_name = goodinfo[3]
        all_comment = goodinfo[-3]
        price = goodinfo[-2]
        info.append(good_name)
        info.append(all_comment)
        info.append(price)
        goods_dic[PID] = info
    # print(len(goods_dic))

# goods_info_list = set()
# goods_list = []
with open(
        'X:/数据库/002-京东2-第三方/{2_3_京东第三方商品详情_入库}[店铺ID,VID,PID,主商品ID,商品ID,品牌ID,品牌名称,CID1,CID2,CID3,类目名称1,类目名称2,类目名称3,是否ebook,价格,总评论数,真实评论数,商品名称,数据月份].txt',
        'r', encoding='utf-8') as f:
    for x in tqdm(f):
        good_x_info = x.replace('\n', '').split(',')
        PID_x = good_x_info[4]
        try:
            # 商品名称
            good_x_info[-2] = goods_dic[PID_x][0]
            # 商品评论
            good_x_info[-4] = goods_dic[PID_x][1]
            # 商品价格
            good_x_info[-5] = goods_dic[PID_x][2]
        except:
            pass
        goods_info_str = (',').join(good_x_info)
        with open(
                save_path + '{jd_goodsinfo}[店铺ID,VID,PID,主商品ID,商品ID,品牌ID,品牌名称,CID1,CID2,CID3,类目名称1,类目名称2,类目名称3,是否ebook,价格,总评论数,真实评论数,商品名称,数据月份].txt',
                'a', encoding='utf-8') as f:
            f.write(goods_info_str + '\n')
            # print(goods_info_str)
