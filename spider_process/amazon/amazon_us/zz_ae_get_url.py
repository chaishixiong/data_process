from tqdm import tqdm

f2 = open(r'X:/数据库/欧洲亚马逊/{new_中东单页商品url}[url].txt', 'w', encoding='utf-8')
with open(r'X:/数据库/欧洲亚马逊/{中东亚马逊商品单页_页数_去重}[seller_id,页数].txt', 'r', encoding='utf-8') as f:
    res = f.readlines()
    result = dict()
    # print(res)
    for i in res:
        i = i.replace('\n', '')
        i = i.split(',')
        if int(i[1]) > 20:
            result[i[0]] = [n for n in range(1, 21)]
        else:
            result[i[0]] = [n for n in range(1, int(i[1])+1)]
    for k,v in tqdm(result.items()):
        # print(k,v)
        for m in v:
            # print(k, m)
            url = f'https://www.amazon.ae/s?me={k}&page={m}'
            f2.write(url + '\n')