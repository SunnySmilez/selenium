from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def main():
    # 设置Chrome浏览器驱动路径
    driver_path = '/Users/zhouzhi/Downloads/chromedriver_mac_arm64/chromedriver'

    # 创建Chrome驱动程序的Service对象
    service = Service(driver_path)
    # 创建Chrome浏览器实例
    driver = webdriver.Chrome(service=service)

    # 打开网页
    url = 'https://uk.craftdlondon.com/collections/bestsellers?page=2'
    driver.get(url)

    # 模拟页面滚动到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 获取所有的img标签
    images = driver.find_elements(By.XPATH, "//img")

    # 输出所有img标签的src属性值
    for image in images:
        print(image.get_attribute("src"))

    # 关闭浏览器
    driver.quit()

if __name__ == '__main__':
    main()