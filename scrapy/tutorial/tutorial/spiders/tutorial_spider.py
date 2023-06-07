import scrapy
from tutorial.items import TutorialItem

class TutorialSpider(scrapy.Spider):
    name = "tutorial"
    allowed_domains = ["craftdlondon.com"]
    start_urls = [
        "https://uk.craftdlondon.com/collections/bestsellers?page=2"
    ]

    def parse(self, response):
        product_grid = response.css("ul#product-grid")
        #self.log(f"Product grid: {product_grid.get()}")  # 输出product grid的HTML内容
        products = product_grid.css("li.grid__item")

        filename = "tutorial.csv"
        #with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
        #    writer = csv.writer(csvfile)
        #    writer.writerow(["标题", "价格", "图片"])

        for product in products:
            item = TutorialItem()
            title = product.css("h3.card__heading a::text").get().strip()
            self.log(f"Title: {title}")  # 输出商品标题
            price = product.css("div.price__container .price__regular .price-item--regular::text").get()
            self.log(f"Price: {price}")  # 输出商品价格
            image = product.css("img.motion-reduce::attr(src)").get()
            self.log(f"Image: {image}")  # 输出商品图片URL
            if image and image.startswith("//"):
                image = "https:" + image
            item['title'] = title
            item['price'] = price
            item['image'] = image
            yield item
            #writer.writerow([title, price, image])
        self.log("Scraping finished. Product data saved to 'products.csv'")