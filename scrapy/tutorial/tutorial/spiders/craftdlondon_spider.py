import scrapy

class CraftdlondonSpider(scrapy.Spider):
    name = "Craftdlondon"
    allowed_domains = ["craftdlondon.com"]
    start_urls = [
        "https://uk.craftdlondon.com/collections/bestsellers?page=2"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

