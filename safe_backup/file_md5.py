import hashlib
import time


def getMD5(path):
    d5 = hashlib.md5()  # 生成一个hash的对象
    with open(path, 'rb') as f:
        num=0
        while True:
            num+=1
            content = f.read(1048576)
            if not content:
                break
            d5.update(content)  # 每次读取一部分，然后添加到hash对象里
        print(num)
    # print('MD5 : %s' % d5.hexdigest())
    return d5.hexdigest()  # 打印16进制的hash值


def getSha512(path):
    f = open(path, 'rb')
    sh = hashlib.sha512()
    with open(path, 'rb') as f:
        while True:
            content = f.read(40960)
            if not content:
                break
            sh.update(content)
    # print(sh.hexdigest())
    return sh.hexdigest()


# 装饰器，计算时间用的

def timer(name):  # 高阶函数：以函数作为参数
    def deco1(func):
        def deco(*args, **kwargs):  # 嵌套函数，在函数内部以 def 声明一个函数,接受 被装饰函数的所有参数
            time1 = time.time()
            md5 = func(*args, **kwargs)
            time2 = time.time()
            use_time = round(time2 - time1, 1)
            print('Elapsed %ss' % (use_time),name)
            return md5
        return deco

    return deco1  # 注意，返回的函数没有加括号！所以返回的是一个内存地址，而不是函数的返回值


@timer("xc")
def walk(path):
    md5 = getMD5(path)
    return md5


if __name__ == "__main__":
    # a = walk("G:\下载\mysql-installer-community-8.0.19.0.msi")
    # print(a)
    walk(r"C:\Users\Administrator\Desktop\跨境重点\亚马逊\amazon_sortshop-data0902.txt")