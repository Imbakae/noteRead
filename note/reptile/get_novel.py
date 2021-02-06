import re

from selenium import webdriver

# 目录主页
from selenium.webdriver.chrome.options import Options

base_url = 'http://www.loubiqu.com/10_10582/'


# 获取章节目录 以及章节页面链接
def get_catalogue():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(base_url)

    # 目录列表
    catalogue = {}

    # Xpath筛选
    results = driver.find_elements_by_xpath("//div[contains(@id,'list')]//dl//dd//a")

    for result in results:
        res_url = result.get_attribute('href')  # url
        res_tit = result.text  # 章节标题

        # 检测'月票' '通知' 关键字
        flag = False
        if not re.search('月票', res_tit) and not re.search('通知', res_tit):
            flag = True

        # 存入字典
        if res_url not in catalogue and flag:
            catalogue[res_tit] = res_url

    driver.close()
    # 输出章节总数
    print(catalogue.__len__())
    return catalogue


get_catalogue()
