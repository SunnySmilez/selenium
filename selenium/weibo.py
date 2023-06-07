from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 设置Chrome选项（可选）  
chrome_options = Options()
# 以无头模式运行（可选）  
chrome_options.add_argument("--headless")

# 指定浏览器驱动路径  
driver_path = "/Users/zhouzhi/Downloads/chromedriver_mac64/chromedriver"  # 替换为你的ChromeDriver路径

# 初始化webdriver  
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# 访问目标网页  
url = "https://www.zhipin.com/web/geek/job?query=%E8%BF%90%E8%90%A5&city=101010100"  # 替换为你要访问的JavaScript渲染页面的URL
driver.get(url)

# 等待页面加载完成（可选）  
driver.implicitly_wait(10)  # 设置等待时间，根据实际情况调整  

# 获取页面源代码  
page_source = driver.page_source
print(page_source)
# 在此处添加提取数据的逻辑，例如使用BeautifulSoup或lxml解析HTML  

# 关闭webdriver  
driver.quit()
