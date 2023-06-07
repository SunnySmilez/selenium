import scrapy
from selenium import webdriver
import scrapy
from scrapy.crawler import CrawlerProcess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    start_urls = ['https://www.zhihu.com/signin']

    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        self.check_login_status()

    def check_login_status(self):
        # 等待登录表单加载完成
        login_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'SignFlow'))
        )

        # 检查是否已经登录
        if 'SignFlow-tab--active' in login_form.get_attribute('innerHTML'):
            # 检查当前登录方式是否为密码登录
            password_tab = login_form.find_element(By.XPATH, './/div[@role="button" and text()="密码登录"]')
            if 'SignFlow-tab--active' not in password_tab.get_attribute('class'):
                # 切换到密码登录
                password_tab.click()

                # 填写用户名和密码并提交登录表单
                username_input = login_form.find_element(By.XPATH, './/input[@name="username"]')
                password_input = login_form.find_element(By.XPATH, './/input[@name="password"]')

                username_input.clear()
                username_input.send_keys('15580818723')  # 替换为您的用户名

                password_input.clear()
                password_input.send_keys('Chinadds813')  # 替换为您的密码

                submit_button = login_form.find_element(By.XPATH, './/button[@type="submit"]')
                submit_button.click()

                # 登录成功后调用提问方法
                self.ask_question()
        else:
            # 已经登录，直接调用提问方法
            self.ask_question()

    def ask_question(self):
        ask_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="Button SearchBar-askButton"]'))
        )
        ask_button.click()

        # 在提问页面填写相关信息并提交表单
        question_form = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//form[@class="QuestionForm-main"]'))
        )

        # 填写问题标题
        title_input = question_form.find_element(By.XPATH, './/input[@name="title"]')
        title_input.send_keys('hellword')  # 替换为您的问题标题


# 填写问题描述
        description_input = question_form.find_element(By.XPATH, './/textarea[@name="detail"]')
        description_input.send_keys('helloworld')  # 替换为您的问题描述

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(ZhihuSpider)
    process.start()