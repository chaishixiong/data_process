import asyncio, random
from pyppeteer import launch
from lxml import etree


async def main():
    browser = await launch({'headless': False, 'args': ['--disable-infobars', '--window-size=1920,1080']})
    # page = await browser.newPage()
    browser_context = await browser.createIncognitoBrowserContext()
    page = await browser_context.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto('https://sellerjoin.aliexpress.com/credential/showcredential.htm?storeNum=1102140648')
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.waitFor(2000)
    compent_name = 'shanghaiyuanfandianzishangwuyouxiangongsi'
    await page.type('#searchKey', compent_name, {'delay': input_time_random()})
    await page.click('button[type="button"]')
    await page.waitFor(3000)
    await page.click('span[class="item active"]')
    html_data = await page.content()
    html_xpath_data(html_data)
    await browser.close()
    # await asyncio.sleep(5)
    # slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块，ps：试了好多次都没出滑块
    # if slider:
    #     print('出现滑块')


def html_xpath_data(html_data):
    xpath_data = etree.HTML(html_data)
    company_name = xpath_data.xpath('//tr/td[3]/div/span/span/a/span/text()')
    legal_person = xpath_data.xpath('//span[@class="val"]/span/a/text()')
    register_time = xpath_data.xpath('//span[@class="f"]/span/text()')
    # list_data = []
    num = 2
    a = [register_time[i:i+num] for i in range(0, len(register_time), num)]
    print(company_name)


def input_time_random():
    return random.randint(100, 151)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
