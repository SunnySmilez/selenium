from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def demo():
    # 配置ChromeDriver路径和选项
    driver_path = '/Users/zhouzhi/Downloads/chromedriver_mac_arm64/chromedriver'
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器窗口

    # 初始化ChromeDriver
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    # 打开链接地址
    url = "https://uk.craftdlondon.com/collections/bestsellers"
    driver.get(url)

    # 使用WebDriverWait等待元素出现
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "ProductGridContainer")))
    print(element)


if __name__ == "__main__":
    demo()