from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from fake_useragent import UserAgent                          #随机代理UserAgent
import random                                                 #随机


import time
import requests
def ceshi():
    chrome_options = Options()

    # 设置请求头
    ua=UserAgent()
    user_agent = ua.random
    print(user_agent)
    # 添加请求头到 ChromeOptions
    chrome_options.add_argument(f'user-agent={user_agent}') # 替换User-Agent

    # UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    # chrome_options.add_argument('User-Agent=' + UserAgent)

    # 创建Proxy对象
    proxy_arr = [
        '--proxy-server=http://183.247.211.41:30001',
        #'--proxy-server=http://183.247.211.50:30001',
        #'--proxy-server=http://122.9.101.6:8888',
    ]

    proxy = random.choice(proxy_arr)  # 随机选择一个代理
    print(proxy) #如果某个代理访问失败,可从proxy_arr中去除
    chrome_options.add_argument(proxy)  # 添加代理
    #chrome_options.add_argument("--proxy-server=http://82.180.163.163:80")


    '''proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = '45.62.167.249:80'  # 代理IP地址和端口
    # 创建DesiredCapabilities对象
    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)
    # 使用代理IP, ChromeOptions 启动浏览器
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)
    '''
    driver = webdriver.Chrome(options=chrome_options)

    #boss.get('https://www.zhipin.com/beijing/?sid=sem_pz_bdpc_dasou_title')
    #driver.get('https://www.zhipin.com/c100010000/?query=python&ka=sel-city-100010000')
    #print(boss.get_attribute('innerHTML'))
    #wait = WebDriverWait(driver, 10)
    #element = wait.until(EC.presence_of_element_located((By.ID, 'wrap')))

    # 查看是否代理设置成功
    #driver.get("https://2023.ip138.com/")
    #print(driver.page_source)
    driver.get("http://httpbin.org/get")
    print(driver.page_source)


    driver.quit()

    '''input = boss.find_element(By.CLASS_NAME , 'ipt-wrap input')
    putton = boss.find_element(By.CLASS_NAME, 'btn-search')
    input.send_keys('运营')
    putton.click()
    html = boss.page_source
    print(html)'''


    ''' 
    boss.implicitly_wait(10)
    ul = boss.find_element(By.CLASS_NAME,'page-job-inner')
    list = ul.find_elements(By.CLASS_NAME,'job-card-wrapper')
    print(ul)
    '''
#    for li in list:

    '''        
        print('bbb')
        biaoti = li.find_elements(By.CLASS_NAME, 'company-info a')
        print(biaoti)
    '''

def isUseful():
    url = "http://httpbin.org/ip"
    proxy_pool = [
        "http://117.64.236.35:9999"
        "http://27.192.202.158:9000",
        "http://36.134.91.82:8888",
        "http://183.236.232.160:8080",
        "http://183.247.211.41:30001",
    ]

    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    for proxy in proxy_pool:
        proxies = {
            "http": proxy,
            "https": proxy,
        }

        start_time = time.time()
        try:
            response = requests.get(url, proxies=proxies, headers=headers, timeout=5)
            elapsed_time = time.time() - start_time

            if response.status_code == 200:
                print(f"代理IP {proxy} 可用，响应时间：{elapsed_time:.2f}秒")
            else:
                print(f"代理IP {proxy} 请求失败，状态码：{response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"代理IP {proxy} 发生异常：{e}")

if __name__ == "__main__":
    isUseful()
    #ceshi()