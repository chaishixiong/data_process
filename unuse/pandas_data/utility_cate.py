# coding=utf-8

class CCate:
    other_cn = '其他'

    ec_list = [
        'taobao',
        'tmall',
        'jd',
        # 'yhd',
        'suning',
        'gome',
        # 'amazon',
        'taobao_qiye'
    ]
    #
    cate_list = [
        '食品保健',
        '3C数码',
        '家居家装',
        '服饰鞋包',
        '文化娱乐',
        '美装护肤',
        '机车配件',
        '生活服务',
        '母婴用品',
        '运动户外',
        '其他'
    ]

    dr = './输入数据/行业分类数据'
    ec_cate_norm = {}

    def __init__(self):
        for ec in self.ec_list:
            self.ec_cate_norm[ec] = {}
            fr_name = '{}_行业分类.csv'.format(ec)
            fr = open('{}/{}'.format(self.dr, fr_name))

            for line in fr:
                cate, norm_cate = line.strip().split(',')
                # print(cate)
                self.ec_cate_norm[ec][cate] = norm_cate
            fr.close()

    def get_ec_cate_norm(self, ec, cate):
        if cate is None:
            return self.other_cn
        cate = cate.strip().split(' ')[0]
        if cate in self.ec_cate_norm[ec].keys():
            return self.ec_cate_norm[ec][cate]

        if cate != '' and cate.lower() != 'null' and cate.lower() != 'none':
            print(ec, ' 主营业务为“' + cate + '”，分类为“' + self.other_cn + '”，请核对是否正确')
        return self.other_cn


ccate = CCate()

