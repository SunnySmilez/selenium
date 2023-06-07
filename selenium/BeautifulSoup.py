from selenium.webdriver.chrome.service import Service
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

def Beau():
    # 初始化 ChromeDriver

    webdriver_service = Service('/Users/zhouzhi/Downloads/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(service=webdriver_service)

    # 待爬取的 URL
    url = 'https://uk.craftdlondon.com/collections/bestsellers'

    # 以写入模式打开 CSV 文件，设置编码格式并写入表头
    csv_file = open('product.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(['标题', '价格', '图片链接'])

    # 爬取所有分页的产品数据

    # 发送 GET 请求获取网页内容

    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # 找到产品列表并遍历获取每个产品的图片、标题和价格
    product_list = soup.find_all('div', {'class': 'product-card'})
    print(product_list)
    for product in product_list:
        title = product.find('a', {'class': 'product-card__title-link'}).text
        price = product.find('span', {'class': 'product-card__price'}).text.replace('\n', '')
        img = product.find('img', {'class': 'product-card__image'})
        img_url = img.attrs.get('data-src') if img else ''
        writer.writerow([title, price, img_url])

    # 找到下一页按钮并点击
        next_page_link = soup.find('a', {'class': 'pagination__item--next'})
        if next_page_link is None:

            break

        else:
            url = next_page_link.attrs['href']
            driver.find_element_by_css_selector('.pagination__item--next').click()
            time.sleep(2) # 等待页面加载完

    # 关闭 CSV 文件并退出浏览器
    csv_file.close()
    driver.quit()

if __name__ == "__main__":
    Beau()