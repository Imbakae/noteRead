from selenium import webdriver

# 目录主页
from selenium.webdriver.chrome.options import Options

base_url = 'http://www.loubiqu.com/10_10582/'


# 获取章节目录 以及章节页面链接
def get_catalogue():
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_option=chrome_option)
    driver.get(base_url)

    # 目录列表
    cateloge = {}

    # Xpath筛选
    results = driver.find_elements_by_xpath("//div[contains(@id,'list')]//dl//dd//a")
    print(results)


get_catalogue()
