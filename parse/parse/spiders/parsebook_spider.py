import scrapy

class BookSpider(scrapy.Spider):
    name = 'parsebook'
    start_urls = ['http://books.toscrape.com/catalogue/page-%s.html' % page for page in xrange(1,51)]
    def parse(self, response):
        for title in response.css('.product_pod a::attr(title)').extract():
            print(title)
