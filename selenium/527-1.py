from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 设置 ChromeDriver 的路径
webdriver_service = Service('/Users/zhouzhi/Downloads/chromedriver_mac_arm64/chromedriver')

# 设置 ChromeDriver 的选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式，可选
chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速，可选

# 创建 Chrome WebDriver 实例
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# 定义初始页面 URL
start_url = "https://www.cnpcbidding.com/html/1/index.html"

# 定义指定关键词
keyword = "招标公告"

# 定义一个列表，用于存储招标公告信息
tender_notices = []

# 递归函数，用于获取指定网页及其子页面的招标公告信息
def get_tender_notices(url):
    # 导航到页面
    driver.get(url)
    # 获取页面源代码
    html = driver.page_source
    # 使用 BeautifulSoup 解析页面
    soup = BeautifulSoup(html, "html.parser")
    # 查找招标公告信息
    notices = soup.find_all(string=lambda t: t and keyword in t)
    # 将招标公告信息添加到列表中
    tender_notices.extend(notices)
    # 查找下一页链接
    next_page_link = soup.find("a", string="下一页")
    if next_page_link:
        next_page_url = next_page_link["href"]
        # 递归调用函数，获取下一页的招标公告信息
        get_tender_notices(next_page_url)

if __name__ == "__main__":
    # 开始获取招标公告信息
    get_tender_notices(start_url)

    # 输出招标公告信息
    for notice in tender_notices:
        print(notice)

    # 关闭 WebDriver
    driver.quit()

