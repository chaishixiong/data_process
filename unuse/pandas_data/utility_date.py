# coding=utf-8


class CDate:

    # 输入一对日期，如(201612, 201702)，
    # 返回日期列表，如['201612', '201701', '201702']

    def get_ym_list(self, yma, ymb=None):
        if ymb is None:
            return [str(yma)]

        if str(yma) == str(ymb):
            return [str(yma)]

        yya = int(str(yma)[:4])
        mma = int(str(yma)[4:])

        yyb = int(str(ymb)[:4])
        mmb = int(str(ymb)[4:])

        isReverse = False
        if (yya > yyb) or ((yya == yyb) and (mma > mmb)):
            isReverse = True

            tmp = yya
            yya = yyb
            yyb = tmp

            tmp = mma
            mma = mmb
            mmb = tmp

        if isReverse:
            ym_list = [str(ymb)]
        else:
            ym_list = [str(yma)]

        while (yya != yyb) or (mma != mmb):
            mma = mma + 1
            if mma % 12 == 1:
                mma = 1
                yya = yya + 1
            yystr = str(yya)
            if mma < 10:
                mmstr = '0' + str(mma)
            else:
                mmstr = str(mma)
            ym_list.append(yystr + mmstr)

        if isReverse:
            ym_list.reverse()

        return ym_list

    def get_yy_dot_mm(self, ym):
        return '{}.{}'.format(ym[:4], ym[4:])

    def get_ym_cn(self, ym):
        return '{}年{}月'.format(ym[:4], ym[4:])

    # 前n个月的年月
    def get_ym_prev(self, ym, n):
        yr = int(str(ym)[:4])
        mn = int(str(ym)[4:])

        n_yr = n // 12
        n_mn = n % 12

        yr_prev = yr - n_yr
        mn_prev = mn - n_mn

        if mn_prev > 0:
            if mn_prev < 10:
                return '{}0{}'.format(yr_prev, mn_prev)
            else:
                return '{}{}'.format(yr_prev, mn_prev)

        mn_prev += 12
        yr_prev -= 1

        if mn_prev < 10:
            return '{}0{}'.format(yr_prev, mn_prev)

        return '{}{}'.format(yr_prev, mn_prev)

cdate = CDate()


quarter_list = [None, '第一季度', '第二季度', '第三季度', '第四季度']
quarters_list = [None, '一季度', '二季度', '三季度', '四季度']

quarter_mn = {'第一季度': ['01', '02', '03'],
              '第二季度': ['04', '05', '06'],
              '第三季度': ['07', '08', '09'],
              '第四季度': ['10', '11', '12']}











