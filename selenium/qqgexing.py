from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

from bs4 import BeautifulSoup

def scrape_images():
    options = webdriver.ChromeOptions()
    # 设置 WebDriver 的路径
    webdriver_service = Service('/Users/zhouzhi/Downloads/chromedriver_mac_arm64/chromedriver')

    # 创建 Chrome WebDriver
    driver = webdriver.Chrome(service=webdriver_service, options=options)

    driver.get('https://www.woyaogexing.com/touxiang/')

    #获取图片元素
    while True:
        #获取图片元素
        tupian = driver.find_elements(By.CSS_SELECTOR, '.txList .img img')
        for imges in tupian:
            outer_html = imges.get_attribute("outerHTML")
            print(outer_html)

            imges_url = imges.get_attribute('src')
            print(imges_url)
            file_name = "./page_img/"+imges_url.split('/')[-1]
            save_image(imges_url,file_name)

#检查是否有按钮
#获取按钮元素
        anniu = driver.find_elements(By.CSS_SELECTOR, '.page a')
        kong = None
        for xiaye in anniu:
            if xiaye.text == '下一页':
                kong = xiaye
                break

            if not kong:
                 break
        #点击按钮
        kong.click()


#关闭网站
        driver.quit()


#保存文件
def save_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image {filename} downloaded successfully.")
    else:
        print(f"Failed to download image {filename}.")

if __name__ == '__main__':
    tupian = scrape_images()





