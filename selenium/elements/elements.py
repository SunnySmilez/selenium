from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# https://www.selenium.dev/zh-cn/documentation/webdriver/elements/finders/
def test():
    # 设置Chrome浏览器驱动路径
    driver_path = '/Users/zhouzhi/Downloads/chromedriver_mac64/chromedriver'

    # 创建Chrome驱动程序的Service对象
    service = Service(driver_path)
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(service=service, options=options)

    # 打开目标网页
    file_path = "/Users/zhouzhi/python-script/elements/elements.html"
    url = f'file://{file_path}'
    driver.get(url)
    driver.implicitly_wait(10)
    a = driver.find_element(By.CLASS_NAME, "tomatoes")
    print(a.text)

    fruits = driver.find_element(By.ID, "fruits")
    fruit = fruits.find_element(By.CLASS_NAME,"tomatoes")
    print(fruit.text)

    b = driver.find_element(By.CSS_SELECTOR, "#fruits .tomatoes")
    print(b.text)

    plants = driver.find_elements(By.TAG_NAME, "li")
    for plant in plants:
        print(plant.text)

def active():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

    # Get attribute of current active element
    attr = driver.switch_to.active_element.get_attribute("title")
    print(attr)

if __name__ == '__main__':
    #test()
    active()