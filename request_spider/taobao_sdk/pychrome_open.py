# -*- coding: utf-8 -*-
import asyncio
from pyppeteer import launch

# js脚本为了屏蔽淘宝的工具检测
js1 = '''() =>{
           Object.defineProperties(navigator,{
             webdriver:{
               get: () => false
             }
           })
        }'''

js2 = '''() => {
        alert (
            window.navigator.webdriver
        )
    }'''

js3 = '''() => {
        window.navigator.chrome = {
    runtime: {},
    // etc.
  };
    }'''

js4 = '''() =>{
Object.defineProperty(navigator, 'languages', {
      get: () => ['en-US', 'en']
    });
        }'''

js5 = '''() =>{
Object.defineProperty(navigator, 'plugins', {
    get: () => [1, 2, 3, 4, 5,6],
  });
        }'''


# 登录函数
async def login(page):
    # 进入登录页面，运行js，填写用户名，密码
    # await page.setUserAgent(
    #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    # await page.goto('https://h5.m.taobao.com/awp/core/detail.htm?id=609648736425')
    slider = 0
    if slider:
        print('当前页面出现滑块')
        # await page.screenshot({'path': './headless-login-slide.png'}) # 截图测试
        # statue = await self.mouse_slide()
    # 跳转首页，打印cookie
    # await page.goto('https://www.taobao.com')
    cookies2 = await page.cookies()
    aaaa = await page.content()
    print(cookies2)


# 主函数
async def main():
    # 初始化浏览器
    browser = await launch({
        'handleSIGINT': False,
        'handleSIGTERM': False,
        'handleSIGHUP': False,
        'headless': False,
        'dumpio': True,
        'args': [
            '--no-sandbox',
            '--no-default-browser-check',
            '--disable-extensions',
            '--hide-scrollbars',
            '--disable-bundled-ppapi-flash',
            '--mute-audio',
            '--disable-setuid-sandbox',
            '--disable-gpu',
            "--window-size=1500,900",
            "--disable-infobars"  # 禁止提示 浏览器被驱动的提示信息
        ],
    })
    page = await browser.newPage()  # "通过 Browser 对象创建页面 Page 对象"
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
    await page.setViewport({"width": 1920, "height": 1080})  # 改变 页面大小

    login_url = "https://h5.m.taobao.com/awp/core/detail.htm?id=609648736425"
    await page.goto(login_url)
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                          '{ webdriver:{ get: () => false } }) }')
    # 登录函数
    await login(page)


def open_goods():
    import redis
    with open(r"W:\scrapy_xc\taobao_618_look-data_ll\good_seet.txt", "r",encoding="utf-8") as f:
        goods_str = f.read()
        f.close()
    redisPool = redis.ConnectionPool(host='192.168.0.225', port=5208, db=0, decode_responses=True)
    redis = redis.Redis(connection_pool=redisPool)
    good_list = goods_str.split('\n')
    for goods in good_list:
        redis.sadd('tm_618_goods:request_goods', goods)


# 运行入口
if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(main())
    open_goods()