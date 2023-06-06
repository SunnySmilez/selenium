import scrapy
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class QuotesSpider(scrapy.Spider):
    name = "ceshi"
    start_urls = ["https://www.woyaogexing.com/touxiang/katong/2023/1284241.html"]

    def parse(self, driver):
        os.makedirs('./head/', exist_ok=True)
        # 获取图片元素
        img_element = driver.css( '.class-name[name="artCont"]')

        img_fz = driver.xpath('//li')
        for tp in img_fz:
            tp.xpath('//img')
            image_url =tp.xpath('@src')
        #记录image_url内容
            print(image_url)

            if image_url:
                # 下载图片到指定目录
                save_path = os.path.join('./head/', "image.png")
                driver.execute_script(f"arguments[0].setAttribute('download', '{save_path}');", img_element)
                img_element.screenshot(save_path)
                print(f"Downloaded image: {save_path}")

    # 获取图片链接

