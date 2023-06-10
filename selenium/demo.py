from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def demo():
    # 设置 ChromeDriver 的路径
    webdriver_service = Service('/Users/zhouzhi/Downloads/chromedriver_mac64/chromedriver')

    # 设置 ChromeDriver 的选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式，可选
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速，可选

    # 创建 Chrome WebDriver 实例
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # 导航到页面
    url = "https://www.woyaogexing.com/touxiang/katong/2023/1284241.html"
    driver.get(url)

    # 查找 ul 元素
    ul_element = driver.find_element(By.CSS_SELECTOR, "ul.artCont.cl")

    # 查找 ul 元素下的所有图片元素
    img_elements = ul_element.find_elements(By.TAG_NAME, "img")

    # 遍历图片元素并下载图片
    for img_element in img_elements:
        # 获取图片地址
        img_url = img_element.get_attribute("src")

        # 下载图片逻辑
        # 可以使用第三方库如 requests 或 urllib 来下载图片
        # 这里只是简单示例，将图片地址打印出来
        print("Image URL:", img_url)

    # 关闭 WebDriver
    driver.quit()

if __name__ == "__main__":
    demo()
