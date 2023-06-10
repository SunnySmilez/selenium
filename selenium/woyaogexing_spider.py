from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

from bs4 import BeautifulSoup

def scrape_images():
    options = webdriver.ChromeOptions()
    # 设置 WebDriver 的路径
    webdriver_service = Service('/Users/zhouzhi/Downloads/chromedriver_mac64/chromedriver')

    # 创建 Chrome WebDriver
    driver = webdriver.Chrome(service=webdriver_service, options=options)

    # 导航到目标网页
    driver.get('https://www.woyaogexing.com/touxiang/')

    # 用于保存所有图片链接的列表
    while True:
        # 获取当前页面的所有图片链接
        images = driver.find_elements(By.CSS_SELECTOR, '.txList .img img')
        for image in images:
            image_url = image.get_attribute('src')
            file_name = "./page_img/"+image_url.split('/')[-1]
            save_image(image_url, file_name)
            print(f'Saved image {file_name}.')

        # 检查是否有下一页按钮
        page_links = driver.find_elements(By.CSS_SELECTOR, '.page a')
        next_page_link = None
        for link in page_links:
            if link.text == '下一页':
                next_page_link = link
                break

        if not next_page_link:
            break

         #点击下一页按钮
        next_page_link.click()

    # 关闭 WebDriver
    driver.quit()

def save_image(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image {filename} downloaded successfully.")
    else:
        print(f"Failed to download image {filename}.")

# 实现一个demo函数 对www.baidu.com发起request请求
def demo():
    response = requests.get('https://www.baidu.com')
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    images = scrape_images()

