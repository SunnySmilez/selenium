import scrapy
import csv

class PageSpider(scrapy.Spider):
    name = "page"
    start_urls = ["https://uk.craftdlondon.com/collections/bestsellers"]
    def parse(self, response):
        product_grid = response.css("ul#product-grid")
        #self.log(f"Product grid: {product_grid.get()}")  # 输出product grid的HTML内容
        products = product_grid.css("li.grid__item")

        with open("page.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["标题", "价格", "图片"])

            for product in products:
                title = product.css("h3.card__heading a::text").get().strip()
                #self.log(f"Title: {title}")  # 输出商品标题
                price = product.css("div.price__container .price__regular .price-item--regular::text").get()
                #self.log(f"Price: {price}")  # 输出商品价格
                image = product.css("img.motion-reduce::attr(src)").get()
                #self.log(f"Image: {image}")  # 输出商品图片URL

                # Extract relative image URL and convert it to absolute URL
                if image and image.startswith("//"):
                    image = "https:" + image

                writer.writerow([title, price, image])

            # 提取下一页的URL
            next_page_url = response.xpath('//a[@aria-label="Next page"]/@href').get()
            self.log(f"Next page URL: {next_page_url}")
            if next_page_url:
                next_page_url="https://uk.craftdlondon.com"+next_page_url
                # 创建新的请求对象，并指定parse()方法作为回调函数
                yield scrapy.Request(url=next_page_url, callback=self.parse)

        self.log("Scraping finished. Product data saved to 'products.csv'")