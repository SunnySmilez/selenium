from selenium import webdriver
from selenium.webdriver.common.by import By

#https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/first_script/
def test_eight_components():
    #打开对应地址
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    #获取title信息
    title = driver.title
    print(title)
    assert title == "Web form"

    #等待时间
    driver.implicitly_wait(10)

    #获取元素
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    #输入内容
    text_box.send_keys("Selenium")
    #点击按钮
    submit_button.click()
    #获取元素
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
    print(message)

    driver.quit()

if __name__ == '__main__':
    test_eight_components()
