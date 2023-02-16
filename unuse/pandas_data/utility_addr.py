# coding = utf-8

# 地址数据处理
class CAddr:

    dr = './输入数据/地址数据'

    prov_list = []
    prov_city = {}
    prov_city_cnty = {}

    prov_simple_dict = {}

    prov_set = set()
    prov_city_set = set()
    prov_city_cnty_set = set()

    tb_addr_norm = {}
    b2c_addr_norm = {}

    tb_except_addr_norm = {}
    tb_invalid_addr = set()

    municipality_norm = {}

    def __init__(self):

        fr_name = '区县级行政区划代码201610_商务厅排序.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        fr.readline()
        for line in fr:
            post_code, prov, city, cnty = line.strip().split(',')

            if prov not in self.prov_list:
                self.prov_list.append(prov)
                self.prov_city[prov] = [city]
                self.prov_city_cnty[prov] = {}
                self.prov_city_cnty[prov][city] = [cnty]

                self.prov_set.add(prov)
                self.prov_city_set.add(','.join([prov, city]))
                self.prov_city_cnty_set.add(','.join([prov, city, cnty]))

            elif city not in self.prov_city[prov]:
                self.prov_city[prov].append(city)
                self.prov_city_cnty[prov][city] = [cnty]

                self.prov_city_set.add(','.join([prov, city]))
                self.prov_city_cnty_set.add(','.join([prov, city, cnty]))

            elif cnty not in self.prov_city_cnty[prov][city]:
                self.prov_city_cnty[prov][city].append(cnty)

                self.prov_city_cnty_set.add(','.join([prov, city, cnty]))

        fr.close()

        for prov in self.prov_list:
            self.prov_simple_dict[prov[:2]] = prov

        fr_name = '淘宝地址标准化.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        for line in fr:
            addr, prov, city = line.strip().split(',')
            self.tb_addr_norm[addr] = [prov, city]

        fr_name = '淘宝特殊地址标准化.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        for line in fr:
            line = line.strip().split(',')
            self.tb_except_addr_norm[line[0]] = [line[1], line[2]]
        fr.close()

        fr_name = '淘宝无效地址.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        for line in fr:
            self.tb_invalid_addr.add(line.strip())
        fr.close()

        fr_name = 'B2C平台地址标准化.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        for line in fr:
            prov, city, cnty, norm_prov, norm_city, norm_cnty = line.strip().split(',')
            addr = ','.join([prov, city, cnty])
            self.b2c_addr_norm[addr] = [norm_prov, norm_city, norm_cnty]
        fr.close()

        fr_name = '直辖市地址标准化.csv'
        fr = open('{}/{}'.format(self.dr, fr_name))
        for line in fr:
            prov, cnty, norm_prov, norm_city, norm_cnty = line.strip().split(',')
            if prov not in self.municipality_norm.keys():
                self.municipality_norm[prov] = {}
                self.municipality_norm[prov][cnty] = [norm_prov, norm_city, norm_cnty]
            elif cnty not in self.municipality_norm[prov]:
                self.municipality_norm[prov][cnty] = [norm_prov, norm_city, norm_cnty]
        fr.close()

    def prov_is_valid(self, prov):
        if prov in self.prov_set:
            return True
        return False

    def prov_city_is_valid(self, prov, city):
        prov_city = '{},{}'.format(prov, city)
        if prov_city in self.prov_city_set:
            return True
        return False

    def prov_city_cnty_is_valid(self, prov, city, cnty):
        prov_city_cnty = '{},{},{}'.format(prov, city, cnty)
        if prov_city_cnty in self.prov_city_cnty_set:
            return True
        return False

    def save_new_addr_norm(self, fw_name, addr, addr_list):
        fw_name = '{}/{}'.format(self.dr, fw_name)
        fw = open(fw_name, 'a')
        fw.write(addr + ',')
        fw.write(','.join(addr_list) + '\n')
        fw.close()

    def save_invalid_addr(self, fw_name, addr):
        fw_name = '{}/{}'.format(self.dr, fw_name)
        fw = open(fw_name, 'a',encoding="utf-8")
        fw.write(addr + '\n')
        fw.close()

    # 寻找两个字符串的最大匹配
    def longest_common_substr(self, s1, s2):

        m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
        longest, x_longest = 0, 0
        for x in range(1, 1 + len(s1)):
            for y in range(1, 1 + len(s2)):
                if s1[x - 1] == s2[y - 1]:
                    m[x][y] = m[x - 1][y - 1] + 1
                    if m[x][y] > longest:
                        longest = m[x][y]
                        x_longest = x
                else:
                    m[x][y] = 0
        return s1[x_longest - longest: x_longest]

    # 返回淘宝标准化后的省份和地市地址
    def get_tb_norm_prov_city(self, addr):

        if addr is None:
            return None, None

        addr = addr.strip()

        if addr in self.tb_addr_norm.keys():
            return self.tb_addr_norm[addr]

        if addr in self.tb_invalid_addr:
            return None, None

        for tb_except_addr in self.tb_except_addr_norm.keys():
            if tb_except_addr in addr:
                norm_prov, norm_city = self.tb_except_addr_norm[tb_except_addr]
                self.tb_addr_norm[addr] = [norm_prov, norm_city]
                self.save_new_addr_norm('淘宝地址标准化.csv', addr, self.tb_addr_norm[addr])
                return norm_prov, norm_city

        tb_prov = addr[:2]
        if tb_prov not in self.prov_simple_dict.keys():
            self.tb_invalid_addr.add(addr)
            self.save_invalid_addr('淘宝无效地址.csv', addr)
            return None, None

        norm_prov = self.prov_simple_dict[tb_prov]

        # 去掉地址中的省份信息
        addr_ori = addr
        max_match = self.longest_common_substr(addr, norm_prov)
        addr = addr.replace(max_match, '')

        # 最大匹配地市信息
        norm_city = None
        max_len = 0
        for city in self.prov_city_cnty[norm_prov].keys():
            str_match = self.longest_common_substr(addr, city)
            if len(str_match) > max_len:
                norm_city = city
                max_match = str_match
                max_len = len(max_match)
        if max_len > 1:
            return norm_prov, norm_city

        for city in self.prov_city_cnty[norm_prov].keys():
            for cnty in self.prov_city_cnty[norm_prov][city]:
                str_match = self.longest_common_substr(addr, cnty)
                if len(str_match) > max_len:
                    norm_city = city
                    max_match = str_match
                    max_len = len(max_match)
        if max_match == '市' or max_match == '县':
            norm_city = None

        if norm_city is not None:
            self.tb_addr_norm[addr_ori] = [norm_prov, norm_city]
            self.save_new_addr_norm('淘宝地址标准化.csv', addr_ori, self.tb_addr_norm[addr_ori])
        else:
            self.tb_invalid_addr.add(addr_ori)
            self.save_invalid_addr('淘宝无效地址.csv', addr_ori)

        return norm_prov, norm_city

    # 返回B2C平台标准化后的省份、地市和区县地址
    def get_b2c_prov_city_cnty(self, prov, city, cnty):
        if self.prov_city_cnty_is_valid(prov, city, cnty):
            return prov, city, cnty

        addr = '{},{},{}'.format(prov, city, cnty)
        if addr in self.b2c_addr_norm.keys():
            return self.b2c_addr_norm[addr]

        if prov is None:
            return None, None, None
        if city is None:
            return None, None, None
        if cnty is None:
            return None, None, None

        prov = prov.strip()
        city = city.strip()
        cnty = cnty.strip()

        if self.prov_city_cnty_is_valid(prov, city, cnty):
            return prov, city, cnty

        addr = '{},{},{}'.format(prov, city, cnty)
        if addr in self.b2c_addr_norm.keys():
            return self.b2c_addr_norm[addr]

        if prov != '' and city != '' and cnty != '':
            print(' 无效地址：', prov, city, cnty)
        return None, None, None

    def get_b2c_munipalicity_norm(self, prov, city, cnty):
        if prov is None:
            prov = ''
        if city is None:
            city = ''
        if cnty is None:
            cnty = ''
        prov = prov[: 2]
        city = city[: 2]
        cnty = cnty[: 2]
        if prov in self.municipality_norm.keys():
            if city in self.municipality_norm[prov]:
                return self.municipality_norm[prov][city]
            if cnty in self.municipality_norm[prov]:
                return self.municipality_norm[prov][cnty]
        return None, None, None

caddr = CAddr()




























