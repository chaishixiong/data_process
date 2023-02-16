# coding=utf-8

class CEcpt:
    ec_list = ['taobao',
               'tmall',
               'jd',
               'suning',
               'gome',
               ]

    ori_ec_list = ['taobao',
                   'tmall',
                   'jd',
                   'suning',
                   'gome',
                   ]

    ori_b2c_list = ['tmall',
                    'jd',
                    'suning',
                    'gome',]

    new_ec_list = ['taobao_geti',
                   'taobao_qiye',
                   'tmall',
                   'jd',
                   'suning',
                   'gome',
                   ]

    all_ec_list = ['taobao',
                   'taobao_geti',
                   'taobao_qiye',
                   'tmall',
                   'jd',
                   'suning',
                   'gome',
                   ]

    new_b2c_list = ['taobao_qiye',
                    'tmall',
                    'jd',
                    'suning',
                    'gome',
                    ]


    en_cn = {
                'taobao': '淘宝',
                'tmall': '天猫',
                'jd': '京东',
                'suning': '苏宁',
                'gome' : '国美',
                'taobao_qiye': '淘宝企业店',
                'taobao_geren': '淘宝个人店',
                'taobao_geti': '淘宝个人店'
             }

    ec_ps = {
                'taobao': '月销售额',
                'tmall': '月销售额',
                'jd': '总评价数*价格/3.5',
                'suning': '3个月销售额',
                'gome': '总销售额',
                'taobao_qiye': '月销售额',
                'taobao_geren': '月销售额',
                'taobao_geti': '月销售额'
             }

cecpt = CEcpt()