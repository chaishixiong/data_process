# coding=utf-8

class CExcp:
    dr = './输入数据/无效网店数据'
    ec_excp_shop_name = {}
    ec_excp_shop_id = {}

    def __init__(self):
        fr_name = '无效网店名称.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        for line in fr:
            ec, shop_name = line.strip().split(',')
            if ec not in self.ec_excp_shop_name.keys():
                self.ec_excp_shop_name[ec] = set()
            self.ec_excp_shop_name[ec].add(shop_name)

        fr.close()

        fr_name = '无效网店id.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        for line in fr:
            ec, shop_id = line.strip().split(',')
            if ec not in self.ec_excp_shop_id.keys():
                self.ec_excp_shop_id[ec] = set()
            self.ec_excp_shop_id[ec].add(shop_id)
        fr.close()

    def shop_is_valid(self, ec, shop_id, prov, city, cnty='c2c'):
        if ec in self.ec_excp_shop_id.keys():
            if shop_id in self.ec_excp_shop_id[ec]:
                return False
        if prov is None:
            return False
        if city is None:
            return False
        if ec != 'taobao':
            if cnty is None:
                return False
        return True

cexcp = CExcp()













