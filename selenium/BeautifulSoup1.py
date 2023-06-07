import csv
import requests
from bs4 import BeautifulSoup
def ceshi():
    # 发起HTTP请求并获取网页内容
    url = "https://uk.craftdlondon.com/collections/bestsellers"
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    # 找到ul
    ul = soup.find("ul", id="product-grid")

    # 创建CSV文件并写入表头
    csv_file = open("product_data.csv", "w", newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["标题", "图片"])

    if ul:
        li_list = ul.find_all("li", class_="grid__item")
        for li in li_list:
            title = li.find("h3", class_="card__heading").text.strip()

 #           price = li.find("span", class_="money").text.strip()

            image = li.find("img")["src"]

            csv_writer.writerow([title, image])

    # 关闭CSV文件
    csv_file.close()


if __name__ == "__main__":
    ceshi()

