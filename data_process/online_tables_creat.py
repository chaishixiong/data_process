import pymysql
def creat_table(sql_prame,sql):
    connect = pymysql.connect(host=sql_prame.get("host"), port=sql_prame.get("port", 3306), db=sql_prame.get("db"),
                              user=sql_prame.get("user"), password=sql_prame.get("password"), charset="utf8",
                              use_unicode=True, cursorclass=pymysql.cursors.SSCursor)
    cursor = connect.cursor()
    result = cursor.execute(sql)
    return result

sql_prame = {
    "host": "192.168.0.227",
    "db": "ec_cross_border",
    "user": "update",
    "password": "change227NRIAT!#$",
    "port":9227
}

creat_sql = ['''
CREATE TABLE `alibabagj_goodsinfo_{}` (
  `goods_url` varchar(255) DEFAULT NULL COMMENT '商品url',
  `goods_name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `goods_id` varchar(30) DEFAULT NULL COMMENT '商品id',
  `price_low` varchar(30) DEFAULT NULL COMMENT '最低价格',
  `price` varchar(30) DEFAULT NULL COMMENT '标准价格',
  `order_min` varchar(255) DEFAULT NULL COMMENT '最小订单量',
  `shop_name` varchar(255) DEFAULT NULL COMMENT '商家名称',
  `shop_url` varchar(255) DEFAULT NULL COMMENT '商家url',
  `export_international` varchar(255) DEFAULT NULL COMMENT '公司地址',
  `rate` varchar(255) DEFAULT NULL COMMENT '公司评论分数',
  `rate_num` varchar(255) DEFAULT NULL COMMENT '公司评论数'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `alibabagj_shopinfo_{}` (
  `key` varchar(255) DEFAULT NULL COMMENT 'key',
  `url` varchar(255) DEFAULT NULL COMMENT '店铺url',
  `company_name` varchar(30) DEFAULT NULL COMMENT '公司名称',
  `address_detail` varchar(30) DEFAULT NULL COMMENT '地址详情',
  `country` varchar(30) DEFAULT NULL COMMENT '国家',
  `province` varchar(255) DEFAULT NULL COMMENT '省',
  `city` varchar(255) DEFAULT NULL COMMENT '市',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `zip` varchar(255) DEFAULT NULL COMMENT '邮编',
  `contact_people` varchar(255) DEFAULT NULL COMMENT '联系人',
  `sales_money` varchar(255) DEFAULT NULL COMMENT '销售金额',
  `sales_num` varchar(255) DEFAULT NULL COMMENT '销售量',
  `company_type` varchar(255) DEFAULT NULL COMMENT '公司类型',
  `keep_time` varchar(255) DEFAULT NULL COMMENT '公司开店时间',
  `province_match` varchar(45) DEFAULT NULL COMMENT '匹配省',
  `city_match` varchar(45) DEFAULT NULL COMMENT '匹配市',
  `area_match` varchar(45) DEFAULT NULL COMMENT '匹配区'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `amazonus_shopinfo_{}` (
  `shop_id` varchar(255) DEFAULT NULL COMMENT '店铺id',
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称',
  `shop_info` varchar(255) DEFAULT NULL COMMENT '店铺介绍',
  `company` varchar(255) DEFAULT NULL COMMENT '公司',
  `company_address` varchar(255) DEFAULT NULL COMMENT '公司地址',
  `country` varchar(255) DEFAULT NULL COMMENT '国家',
  `postcode` varchar(255) DEFAULT NULL COMMENT '邮编',
  `html` text COMMENT '公司原始html',
  `goodrate_month` varchar(255) DEFAULT NULL COMMENT '30天好评率',
  `middlerate_month` varchar(255) DEFAULT NULL COMMENT '30天中评率',
  `badrate_month` varchar(255) DEFAULT NULL COMMENT '30天差评率',
  `comment_month` varchar(255) DEFAULT NULL COMMENT '30天评论数',
  `goodrate_quarterly` varchar(255) DEFAULT NULL COMMENT '90天好评率',
  `middlerate_quarterly` varchar(255) DEFAULT NULL COMMENT '90天中评率',
  `badrate_quarterly` varchar(255) DEFAULT NULL COMMENT '90天差评率',
  `comment_quarterly` varchar(255) DEFAULT NULL COMMENT '90天评论数',
  `goodrate_year` varchar(255) DEFAULT NULL COMMENT '一年好评率',
  `middlerate_year` varchar(255) DEFAULT NULL COMMENT '一年中评率',
  `badrate_year` varchar(255) DEFAULT NULL COMMENT '一年差评率',
  `comment_year` varchar(255) DEFAULT NULL COMMENT '一年评论数',
  `goodrate_total` varchar(255) DEFAULT NULL COMMENT '累计好评率',
  `middlerate_total` varchar(255) DEFAULT NULL COMMENT '累计中评率',
  `badrate_total` varchar(255) DEFAULT NULL COMMENT '累计差评率',
  `comment_total` varchar(255) DEFAULT NULL COMMENT '累计评论数',
  `province` varchar(255) DEFAULT NULL COMMENT '省',
  `city` varchar(255) DEFAULT NULL COMMENT '市',
  `county` varchar(255) DEFAULT NULL COMMENT '区',
  `main_sales` varchar(255) DEFAULT NULL COMMENT '主营',
  `average_price` varchar(255) DEFAULT NULL COMMENT '平均售价'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''CREATE TABLE `amazonus_shopinfo_{}_sales` (
  `shop_id` varchar(255) DEFAULT NULL COMMENT '店铺id',
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称',
  `shop_info` varchar(255) DEFAULT NULL COMMENT '店铺介绍',
  `company` varchar(255) DEFAULT NULL COMMENT '公司',
  `company_address` varchar(255) DEFAULT NULL COMMENT '公司地址',
  `country` varchar(255) DEFAULT NULL COMMENT '国家',
  `postcode` varchar(255) DEFAULT NULL COMMENT '邮编',
  `html` text COMMENT '公司原始信息',
  `goodrate_month` varchar(255) DEFAULT NULL COMMENT '30天好评率',
  `middlerate_month` varchar(255) DEFAULT NULL COMMENT '30天中评率',
  `badrate_month` varchar(255) DEFAULT NULL COMMENT '30天差评率',
  `comment_month` varchar(255) DEFAULT NULL COMMENT '30天评论数',
  `goodrate_quarterly` varchar(255) DEFAULT NULL COMMENT '90天好评率',
  `middlerate_quarterly` varchar(255) DEFAULT NULL COMMENT '90天中评率',
  `badrate_quarterly` varchar(255) DEFAULT NULL COMMENT '90天差评率',
  `comment_quarterly` varchar(255) DEFAULT NULL COMMENT '90天评论数',
  `goodrate_year` varchar(255) DEFAULT NULL COMMENT '一年好评率',
  `middlerate_year` varchar(255) DEFAULT NULL COMMENT '一年中评率',
  `badrate_year` varchar(255) DEFAULT NULL COMMENT '一年差评率',
  `comment_year` varchar(255) DEFAULT NULL COMMENT '一年评论数',
  `goodrate_total` varchar(255) DEFAULT NULL COMMENT '累计好评率',
  `middlerate_total` varchar(255) DEFAULT NULL COMMENT '累计中评率',
  `badrate_total` varchar(255) DEFAULT NULL COMMENT '累计差评率',
  `comment_total` varchar(255) DEFAULT NULL COMMENT '累计评论数',
  `province` varchar(255) DEFAULT NULL COMMENT '省',
  `city` varchar(255) DEFAULT NULL COMMENT '市',
  `county` varchar(255) DEFAULT NULL COMMENT '区',
  `main_sales` varchar(255) DEFAULT NULL COMMENT '主营',
  `average_price` varchar(255) DEFAULT NULL COMMENT '平均售价',
  `sales` varchar(255) DEFAULT NULL COMMENT '销量',
  `sales_money` varchar(255) DEFAULT NULL COMMENT '销售额',
  `sales_y` varchar(255) DEFAULT NULL COMMENT '年度销量',
  `sales_money_y` varchar(255) DEFAULT NULL COMMENT '年度销售额'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
''','''
CREATE TABLE `amazonus_goodsinfo_{}` (
  `shop_id` varchar(255) DEFAULT NULL COMMENT '店铺id',
  `goods_name` varchar(30) DEFAULT NULL COMMENT '商品名称',
  `comment_rate` varchar(30) DEFAULT NULL COMMENT '评论分数',
  `comment_num` varchar(255) DEFAULT NULL COMMENT '评论数量',
  `url` varchar(30) DEFAULT NULL COMMENT '商品url',
  `price` varchar(30) DEFAULT NULL COMMENT '商品价格',
  `goods_id` varchar(30) DEFAULT NULL COMMENT '商品id',
  `goods_num` varchar(255) DEFAULT NULL COMMENT '回答问题数量',
  `brand` varchar(1021) DEFAULT NULL COMMENT '品牌'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `jdid_goodsinfo_{}` (
  `vender_id` varchar(255) DEFAULT NULL COMMENT '供应商id',
  `total_num` varchar(255) DEFAULT NULL COMMENT '店铺商品数',
  `comment_num` varchar(30) DEFAULT NULL COMMENT '评论数',
  `comment_score` varchar(30) DEFAULT NULL COMMENT '评论分数',
  `img_url` varchar(30) DEFAULT NULL COMMENT '图片url',
  `promo_statu` varchar(255) DEFAULT NULL COMMENT '促销状态',
  `goods_id` varchar(255) DEFAULT NULL COMMENT '商品id',
  `goods_name` varchar(255) DEFAULT NULL COMMENT '商品名称'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `jdid_shopinfo_{}` (
  `vender_id` varchar(255) DEFAULT NULL COMMENT '供应商id',
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称',
  `fans` varchar(30) DEFAULT NULL COMMENT '粉丝数',
  `categorys` varchar(30) DEFAULT NULL COMMENT '类型',
  `goods_num` varchar(30) DEFAULT NULL COMMENT '商品数量'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `newegg_goodsinfo_{}` (
  `sort` varchar(30) DEFAULT NULL COMMENT '分类',
  `url` varchar(255) DEFAULT NULL COMMENT 'url',
  `name` varchar(255) DEFAULT NULL COMMENT '名称',
  `brand` varchar(30) DEFAULT NULL COMMENT '品牌',
  `price` varchar(255) DEFAULT NULL COMMENT '价格',
  `goods_id` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `size` varchar(255) DEFAULT NULL COMMENT '尺寸',
  `type` varchar(255) DEFAULT NULL COMMENT '类型',
  `color` varchar(255) DEFAULT NULL COMMENT '颜色',
  `age` varchar(255) DEFAULT NULL,
  `shop_url` varchar(255) DEFAULT NULL COMMENT '店铺url',
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `shopee_goodsinfo_{}` (
  `shop_id` varchar(255) DEFAULT NULL COMMENT '店铺id',
  `goods_id` varchar(255) DEFAULT NULL COMMENT '商品id',
  `name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `price` varchar(255) DEFAULT NULL COMMENT '描述',
  `currency` varchar(255) DEFAULT NULL COMMENT '货币',
  `totle_num` varchar(255) DEFAULT NULL COMMENT '历史总销量',
  `sales_num` varchar(255) DEFAULT NULL COMMENT '销量',
  `stock` varchar(255) DEFAULT NULL COMMENT '库存',
  `rating_star` varchar(255) DEFAULT NULL COMMENT '评论星级',
  `item_status` varchar(255) DEFAULT NULL COMMENT '退货率',
  `show_free_shipping` varchar(255) DEFAULT NULL COMMENT '是否送貨',
  `brand` varchar(255) DEFAULT NULL COMMENT '品牌',
  `cid` varchar(255) DEFAULT NULL COMMENT '类目id',
  `url` varchar(255) DEFAULT NULL COMMENT 'url',
  `location` varchar(255) DEFAULT NULL COMMENT '店铺属于区域',
  `view_count` varchar(255) DEFAULT NULL COMMENT '查看次数'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `shopee_shopinfo_{}` (
  `shop_id` varchar(255) DEFAULT NULL COMMENT '店铺id',
  `name` varchar(255) DEFAULT NULL COMMENT '商铺名称',
  `description` varchar(255) DEFAULT NULL COMMENT '描述',
  `country` varchar(255) DEFAULT NULL COMMENT '国家',
  `place` varchar(255) DEFAULT NULL COMMENT '地点',
  `follower_count` varchar(255) DEFAULT NULL COMMENT '粉丝数',
  `rating_good` varchar(255) DEFAULT NULL COMMENT '好评论',
  `rating_bad` varchar(255) DEFAULT NULL COMMENT '坏评论',
  `cancellation_rate` varchar(255) DEFAULT NULL COMMENT '退货率',
  `url` varchar(255) DEFAULT NULL COMMENT 'url',
  `item_count` varchar(255) DEFAULT NULL COMMENT 'item',
  `rating_star` varchar(255) DEFAULT NULL COMMENT '评论星级',
  `shop_location` varchar(255) DEFAULT NULL COMMENT '店铺属于区域'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `shopee_sortinfo_{}` (
  `cid` varchar(255) DEFAULT NULL COMMENT '类目id1',
  `cname` varchar(255) DEFAULT NULL COMMENT '类目名称1',
  `cid2` varchar(255) DEFAULT NULL COMMENT '类目id2',
  `cname2` varchar(255) DEFAULT NULL COMMENT '类目名称2',
  `cid3` varchar(255) DEFAULT NULL COMMENT '类目id3',
  `cname3` varchar(255) DEFAULT NULL COMMENT '类目名称3'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `smt_commentinfo_{}` (
  `seller_id` varchar(30) DEFAULT NULL COMMENT '卖家id',
  `good_id` varchar(30) DEFAULT NULL COMMENT '商品id',
  `current_page` varchar(255) DEFAULT NULL COMMENT '当前页数',
  `comment_num` varchar(255) DEFAULT NULL COMMENT '评论数量',
  `comment_distribution` varchar(255) DEFAULT NULL COMMENT '评论数值分布',
  `user_name` varchar(255) DEFAULT NULL COMMENT '评论名称',
  `country` varchar(255) DEFAULT NULL COMMENT '买家国家',
  `comment_score` varchar(255) DEFAULT NULL COMMENT '比例',
  `comment` varchar(255) DEFAULT NULL COMMENT '评论星级',
  `comment_time` varchar(255) DEFAULT NULL COMMENT '评论时间'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `smt_goodsinfo_{}` (
  `shop_id` varchar(30) DEFAULT NULL COMMENT '店铺id',
  `seller_id` varchar(30) DEFAULT NULL COMMENT '卖家id',
  `totle_num` varchar(30) DEFAULT NULL COMMENT '商品数目',
  `good_id` varchar(30) DEFAULT NULL COMMENT '商品id',
  `sales_num` varchar(255) DEFAULT NULL COMMENT '销量',
  `maxPrice` varchar(255) DEFAULT NULL COMMENT '商品价格_较高值',
  `minPrice` varchar(255) DEFAULT NULL COMMENT '商品价格_较低值',
  `url` varchar(255) DEFAULT NULL COMMENT '产品url',
  `ratings` varchar(30) DEFAULT NULL COMMENT '评分',
  `good_name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `comments` varchar(255) DEFAULT NULL COMMENT '评论数量',
  `mediaId` varchar(255) DEFAULT NULL COMMENT '媒体id',
  `imageUrl` varchar(255) DEFAULT NULL COMMENT '图片链接',
  `tagResult` varchar(255) DEFAULT NULL COMMENT '标签'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `smt_monthsales_{}` (
  `shop_id` varchar(30) DEFAULT NULL COMMENT '店铺id',
  `seller_id` varchar(30) DEFAULT NULL COMMENT '卖家id',
  `good_id` varchar(30) DEFAULT NULL COMMENT '商品id',
  `sales` varchar(255) DEFAULT NULL COMMENT '销量',
  `price` varchar(255) DEFAULT NULL COMMENT '价格',
  `comment` varchar(255) DEFAULT NULL COMMENT '评论',
  `comment_new` varchar(255) DEFAULT NULL COMMENT '新评论',
  `comment_month` varchar(255) DEFAULT NULL COMMENT '单月评论',
  `bili` varchar(255) DEFAULT NULL COMMENT '比例',
  `sales_month` varchar(255) DEFAULT NULL COMMENT '评论'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''','''
CREATE TABLE `smt_shopinfo_{}` (
  `shop_id` varchar(255) NOT NULL COMMENT '店铺ID',
  `seller_id` varchar(255) DEFAULT NULL COMMENT '卖家id',
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称',
  `address_y` varchar(255) DEFAULT NULL COMMENT '地址',
  `company` varchar(255) DEFAULT NULL COMMENT '公司名称',
  `shui_id` varchar(255) DEFAULT NULL COMMENT '增值税id',
  `yingye_id` varchar(255) DEFAULT NULL COMMENT '营业id',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `people` varchar(255) DEFAULT NULL COMMENT '联系人',
  `scope` varchar(255) DEFAULT NULL COMMENT '业务范围',
  `shopCreatedAt` varchar(255) DEFAULT NULL COMMENT '创建时间',
  `jiguan` varchar(255) DEFAULT NULL COMMENT '登记机关',
  `province` varchar(45) DEFAULT NULL COMMENT '匹配省',
  `city` varchar(45) DEFAULT NULL COMMENT '匹配市',
  `county` varchar(45) DEFAULT NULL COMMENT '匹配区',
  `sales_num` varchar(255) DEFAULT NULL COMMENT '销量',
  `sales_money` varchar(255) DEFAULT NULL COMMENT '销售额',
  `fans` varchar(255) DEFAULT NULL COMMENT '粉丝数',
  `shop_address` varchar(255) DEFAULT NULL COMMENT '店铺地址',
  `open_time` varchar(255) DEFAULT NULL COMMENT '开店时间',
  `sales_month` varchar(255) DEFAULT NULL COMMENT '浙江当月销量',
  PRIMARY KEY (`shop_id`),
  KEY `indexcompany` (`company`) USING BTREE COMMENT 'xvpan'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
  '''CREATE TABLE `gmarket_shopinfo_{}` (
  `shop_id` varchar(255) DEFAULT NULL COMMENT '店铺id',
  `shop_name` varchar(30) DEFAULT NULL COMMENT '店铺名称',
  `shop_url` varchar(255) DEFAULT NULL COMMENT '店铺url',
  `boss` varchar(255) DEFAULT NULL COMMENT '联系人',
  `phone` varchar(30) DEFAULT NULL COMMENT '电话',
  `fax` varchar(255) DEFAULT NULL COMMENT '传真',
  `num` varchar(255) DEFAULT NULL COMMENT '登记号',
  `email` varchar(255) DEFAULT NULL COMMENT '邮箱',
  `address` varchar(255) DEFAULT NULL COMMENT '地址'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
  '''CREATE TABLE `gmarket_goodinfo_{}` (
  `shop_id` varchar(255) DEFAULT NULL COMMENT '店铺id',
  `goods_id` varchar(30) DEFAULT NULL COMMENT '商品id',
  `goods_name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `goods_url` varchar(255) DEFAULT NULL COMMENT '商品url',
  `price` varchar(30) DEFAULT NULL COMMENT '标准价格',
  `yunfei` varchar(255) DEFAULT NULL COMMENT '运费',
  `comment` varchar(255) DEFAULT NULL COMMENT '评论',
  `sales_count` varchar(255) DEFAULT NULL COMMENT '销量'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
  '''CREATE TABLE `kilimall_goodsinfo_{}` (
  `goods_id` varchar(255) NOT NULL COMMENT '商品id',
  `good_url` varchar(255) NOT NULL COMMENT '商品url',
  `good_name` varchar(255) NOT NULL COMMENT '商品名称',
  `new_price` varchar(255) NOT NULL COMMENT '现价',
  `old_price` varchar(255) NOT NULL COMMENT '原价',
  `shop_id` varchar(255) NOT NULL COMMENT '店铺id',
  `comment_nums` varchar(255) NOT NULL COMMENT '评论数',
  `category` varchar(255) NOT NULL COMMENT '分类'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
  '''CREATE TABLE `kilimall_shopinfo_{}` (
  `shop_url` varchar(255) NOT NULL COMMENT '店铺url',
  `shop_id` varchar(255) NOT NULL COMMENT '店铺id',
  `shop_name` varchar(255) NOT NULL COMMENT '店铺名称',
  `score` varchar(255) NOT NULL COMMENT '评分',
  `category` varchar(255) NOT NULL COMMENT '分类'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `linio_goodsinfo_{}` (
  `shop_name` varchar(255) NOT NULL COMMENT '店铺名称',
  `good_id` varchar(255) NOT NULL COMMENT '商品id',
  `good_name` varchar(255) NOT NULL COMMENT '商品名称',
  `brand` varchar(255) NOT NULL COMMENT '分类',
  `good_score` varchar(255) NOT NULL COMMENT '商品评分',
  `price` varchar(255) NOT NULL COMMENT '商品价格',
  `comment` varchar(255) NOT NULL COMMENT '商品评论',
  `cat1` varchar(255) NOT NULL COMMENT '一级标题',
  `cat2` varchar(255) NOT NULL COMMENT '二级标题',
  `cat3` varchar(255) NOT NULL COMMENT '三级标题',
  `cat4` varchar(255) NOT NULL COMMENT '四级标题'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `linio_shopinfo_{}` (
  `good_id` varchar(255) NOT NULL COMMENT '商品id',
  `shop_name` varchar(255) NOT NULL COMMENT '店铺名称',
  `shop_url` varchar(255) NOT NULL COMMENT '链接',
  `shop_score` varchar(255) NOT NULL COMMENT '评分',
  `cat3` varchar(255) NOT NULL COMMENT '分类'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `fruugo_goodsinfo_{}` (
  `key` varchar(30) DEFAULT NULL COMMENT '商品url',
  `good_name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `price` varchar(255) DEFAULT NULL COMMENT '价格',
  `shop_name` varchar(30) DEFAULT NULL COMMENT '店铺名称',
  `shop_url` varchar(255) DEFAULT NULL COMMENT '店铺url',
  `brand` varchar(255) DEFAULT NULL COMMENT '品牌',
  `category` varchar(255) DEFAULT NULL COMMENT '类别',
  `size` varchar(255) DEFAULT NULL COMMENT '尺寸',
  `goods_id` varchar(255) DEFAULT NULL COMMENT '商品id',
  `ean` varchar(255) DEFAULT NULL COMMENT 'ean',
  `productId` varchar(255) DEFAULT NULL COMMENT '产品id',
  `colour` varchar(255) DEFAULT NULL COMMENT '颜色',
  `description` varchar(255) DEFAULT NULL COMMENT '描述'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `fruugo_shopinfo_{}` (
  `shop_name` varchar(30) DEFAULT NULL COMMENT '店铺名称',
  `shop_url` varchar(255) DEFAULT NULL COMMENT 'url',
  `brand` varchar(255) DEFAULT NULL COMMENT '品牌',
  `category` varchar(255) DEFAULT NULL COMMENT '分类'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `ebay_goodsinfo_{}` (
  `good_id` varchar(30) DEFAULT NULL COMMENT '商品id',
  `good_name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `price_dollar` varchar(255) DEFAULT NULL COMMENT '价格（美元）',
  `price_RMB` varchar(30) DEFAULT NULL COMMENT '单价（人民币）',
  `project_location` varchar(255) DEFAULT NULL COMMENT '项目地点',
  `brand` varchar(255) DEFAULT NULL COMMENT '品牌',
  `seller_name` varchar(255) DEFAULT NULL COMMENT '卖家用户名',
  `sales_count` varchar(255) DEFAULT NULL COMMENT '总销量',
  `cat_1` varchar(255) DEFAULT NULL COMMENT '一级类目',
  `cat_2` varchar(255) DEFAULT NULL COMMENT '二级类目',
  `cat_3` varchar(255) DEFAULT NULL COMMENT '三级类目',
  `cat_4` varchar(255) DEFAULT NULL COMMENT '四级类目',
  `cat_5` varchar(255) DEFAULT NULL COMMENT '五级类目',
  `cat_6` varchar(255) DEFAULT NULL COMMENT '六级类目'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `ebay_usrinfo_{}` (
  `seller_name` varchar(255) DEFAULT NULL COMMENT '卖家用户名_卖家唯一标识符',
  `followers_num` varchar(255) DEFAULT NULL COMMENT '此用户在ebay粉丝数',
  `country` varchar(255) DEFAULT NULL COMMENT '国家',
  `positive_feedback_percent` varchar(255) DEFAULT NULL COMMENT '好评率',
  `Feedback_score` varchar(255) DEFAULT NULL COMMENT '评论评分',
  `Item_s_described_score` varchar(255) DEFAULT NULL COMMENT '描述评分',
  `Communication_score` varchar(255) DEFAULT NULL COMMENT '交流评分',
  `Shipping_time_score` varchar(255) DEFAULT NULL COMMENT '物流评分',
  `Shipping_charges_score` varchar(255) DEFAULT NULL COMMENT '运费评分',
  `seller_text` varchar(255) DEFAULT NULL COMMENT '卖家描述',
  `Positive_feedback` varchar(255) DEFAULT NULL COMMENT '好评数',
  `Neutral_feedback` varchar(255) DEFAULT NULL COMMENT '中评数',
  `Negative_feedback` varchar(255) DEFAULT NULL COMMENT '差评数',
  `views` varchar(255) DEFAULT NULL COMMENT '点击量',
  `Reviews` varchar(255) DEFAULT NULL COMMENT '此用户在ebay的评论数',
  `goods_num` varchar(255) DEFAULT NULL COMMENT '商品数',
  `Member_since` varchar(255) DEFAULT NULL COMMENT '入驻时间',
  `shop_url` varchar(255) DEFAULT NULL COMMENT '店铺链接'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `amazonuk_goodsinfo_{}` (
  `shop_id` varchar(225) DEFAULT NULL COMMENT '店铺id',
  `good_id` varchar(225) DEFAULT NULL COMMENT '商品id',
  `good_name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `scores` varchar(255) DEFAULT NULL COMMENT '商品评分',
  `comment` varchar(255) DEFAULT NULL COMMENT '商品评论数',
  `price` varchar(255) DEFAULT NULL COMMENT '商品价格'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `amazonuk_shopinfo_{}` (
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称',
  `shop_id` varchar(225) DEFAULT NULL COMMENT '店铺id',
  `company` varchar(255) DEFAULT NULL COMMENT '公司名称',
  `type` varchar(255) DEFAULT NULL COMMENT '业务类型',
  `registration` varchar(255) DEFAULT NULL COMMENT '商业登记号',
  `vat` varchar(255) DEFAULT NULL COMMENT '增值税编号',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `score` varchar(255) DEFAULT NULL COMMENT '评分',
  `content` varchar(255) DEFAULT NULL COMMENT '店铺介绍',
  `30good_comment` varchar(255) DEFAULT NULL COMMENT '30天好评率',
  `30zhong_comment` varchar(255) DEFAULT NULL COMMENT '30天中评率',
  `30bad_comment` varchar(255) DEFAULT NULL COMMENT '30天差评率',
  `30_comment_num` varchar(255) DEFAULT NULL COMMENT '30天评论数',
  `90good_comment` varchar(255) DEFAULT NULL COMMENT '90天好评率',
  `90zhong_comment` varchar(255) DEFAULT NULL COMMENT '90天中评率',
  `90bad_comment` varchar(255) DEFAULT NULL COMMENT '90天差评率',
  `90_comment_num` varchar(255) DEFAULT NULL COMMENT '90天评论数',
  `12good_comment` varchar(255) DEFAULT NULL COMMENT '12月好评率',
  `12zhong_comment` varchar(255) DEFAULT NULL COMMENT '12月中评率',
  `12bad_comment` varchar(255) DEFAULT NULL COMMENT '12月差评率',
  `12_comment_num` varchar(255) DEFAULT NULL COMMENT '12月评论数',
  `good_comment` varchar(255) DEFAULT NULL COMMENT '累计好评率',
  `zhong_comment` varchar(255) DEFAULT NULL COMMENT '累计中评率',
  `bad_comment` varchar(255) DEFAULT NULL COMMENT '累计差评率',
  `comment_num` varchar(255) DEFAULT NULL COMMENT '累计评论数',
  `main_sales` varchar(255) DEFAULT NULL COMMENT '主营',
  `average_price` varchar(255) DEFAULT NULL COMMENT '平均价格'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `amazonuk_shopinfo_{}_all` (
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称',
  `shop_id` varchar(225) DEFAULT NULL COMMENT '店铺id',
  `company` varchar(255) DEFAULT NULL COMMENT '公司名称',
  `type` varchar(255) DEFAULT NULL COMMENT '业务类型',
  `registration` varchar(255) DEFAULT NULL COMMENT '商业登记号',
  `vat` varchar(255) DEFAULT NULL COMMENT '增值税编号',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `score` varchar(255) DEFAULT NULL COMMENT '评分',
  `content` varchar(255) DEFAULT NULL COMMENT '店铺介绍',
  `30good_comment` varchar(255) DEFAULT NULL COMMENT '30天好评率',
  `30zhong_comment` varchar(255) DEFAULT NULL COMMENT '30天中评率',
  `30bad_comment` varchar(255) DEFAULT NULL COMMENT '30天差评率',
  `30_comment_num` varchar(255) DEFAULT NULL COMMENT '30天评论数',
  `90good_comment` varchar(255) DEFAULT NULL COMMENT '90天好评率',
  `90zhong_comment` varchar(255) DEFAULT NULL COMMENT '90天中评率',
  `90bad_comment` varchar(255) DEFAULT NULL COMMENT '90天差评率',
  `90_comment_num` varchar(255) DEFAULT NULL COMMENT '90天评论数',
  `12good_comment` varchar(255) DEFAULT NULL COMMENT '12月好评率',
  `12zhong_comment` varchar(255) DEFAULT NULL COMMENT '12月中评率',
  `12bad_comment` varchar(255) DEFAULT NULL COMMENT '12月差评率',
  `12_comment_num` varchar(255) DEFAULT NULL COMMENT '12月评论数',
  `good_comment` varchar(255) DEFAULT NULL COMMENT '累计好评率',
  `zhong_comment` varchar(255) DEFAULT NULL COMMENT '累计中评率',
  `bad_comment` varchar(255) DEFAULT NULL COMMENT '累计差评率',
  `comment_num` varchar(255) DEFAULT NULL COMMENT '累计评论数',
  `main_sales` varchar(255) DEFAULT NULL COMMENT '主营',
  `average_price` varchar(255) DEFAULT NULL COMMENT '平均价格',
  `companys` varchar(255) DEFAULT NULL COMMENT '公司',
  `company_address` varchar(255) DEFAULT NULL COMMENT '公司地址',
  `province` varchar(255) DEFAULT NULL COMMENT '省',
  `city` varchar(255) DEFAULT NULL COMMENT '市',
  `county` varchar(255) DEFAULT NULL COMMENT '县'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `amazonae_goodsinfo_{}` (
  `shop_id` varchar(225) DEFAULT NULL COMMENT '店铺id',
  `good_id` varchar(225) DEFAULT NULL COMMENT '商品id',
  `good_name` varchar(255) DEFAULT NULL COMMENT '商品名称',
  `scores` varchar(255) DEFAULT NULL COMMENT '商品评分',
  `comment` varchar(255) DEFAULT NULL COMMENT '商品评论数',
  `price` varchar(255) DEFAULT NULL COMMENT '商品价格'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''',
             '''CREATE TABLE `amazonae_shopinfo_{}` (
  `shop_name` varchar(255) DEFAULT NULL COMMENT '店铺名称',
  `shop_id` varchar(225) DEFAULT NULL COMMENT '店铺id',
  `company` varchar(255) DEFAULT NULL COMMENT '公司名称',
  `type` varchar(255) DEFAULT NULL COMMENT '业务类型',
  `registration` varchar(255) DEFAULT NULL COMMENT '商业登记号',
  `vat` varchar(255) DEFAULT NULL COMMENT '增值税编号',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `score` varchar(255) DEFAULT NULL COMMENT '评分',
  `comment_num` varchar(255) DEFAULT NULL COMMENT '评论数'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;''']

if __name__ == "__main__":
    month = int(input("202012(除了1月1月要改):"))
    last_month = month - 1
    for i in creat_sql:
        sql = i.format(month)
        try:
            result = creat_table(sql_prame=sql_prame,sql=sql)
            print(result)
        except Exception as e:
            print(e)

