import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.request

def test():
    # 设置Chrome浏览器驱动路径
    driver_path = '/Users/zhouzhi/Downloads/chromedriver_mac64/chromedriver'

    # 创建Chrome驱动程序的Service对象
    service = Service(driver_path)

    # 创建Chrome浏览器实例
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(service=service, options=options)

    # 打开目标网页
    url = 'https://uk.craftdlondon.com/collections/bestsellers?page=2'
    driver.get(url)

    # 等待网页加载完成
    #driver.implicitly_wait(10)

    # 找到所有图片元素
    images = driver.find_elements(By.XPATH, "//img")

    # 指定保存图片的目录
    save_directory = './images'

    # 遍历图片元素并下载图片
    for image in images:
        image_url = image.get_attribute("src")
        image_name = image.get_attribute("alt")
        if image_url and image_name:
            save_path = os.path.join(save_directory, f"{image_name}.jpg")
            urllib.request.urlretrieve(image_url, save_path)
            print(save_path)

    # 关闭浏览器
    driver.quit()

if __name__ == '__main__':
    test()