from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
def ceshi():

#    url = "https://weibo.com/"
#    response = requests.get(url)
#    html_content = response.content
    soup = webdriver.Chrome()
#    soup.implicitly_wait(30)
    soup.get('https://www.jd.com')


#   soup = BeautifulSoup(html_content, "html.parser")
#    print(soup)
    # 找到ul
    input =soup.find_element(By.ID, 'key')
    input.send_keys('鞋子')
    button = soup.find_element(By.CLASS_NAME, 'button')
    button.click()
    print('aaaaa')
    id = soup.find_element(By.ID,'J_goodsList')
    ul = id.find_element(By.CLASS_NAME,'clearfix')
#    print(ul.get_attribute('innerHTML'))
    list = ul.find_elements(By.CLASS_NAME,'gl-i-wrap')

    for li in list:
        img = li.find_element(By.CLASS_NAME,'p-img')
        jiage = li.find_element(By.CSS_SELECTOR, '.p-price i')
        biaoti = li.find_element(By.CSS_SELECTOR, '.p-name em')
        pingjia = li.find_element(By.CSS_SELECTOR, '.p-commit a')
        dianname = li.find_element(By.CSS_SELECTOR, '.p-shop a')
        print(dianname.text)
        href = img.find_element('css selector','a').get_attribute('href')
#        print(href)

if __name__ == "__main__":
    ceshi()

