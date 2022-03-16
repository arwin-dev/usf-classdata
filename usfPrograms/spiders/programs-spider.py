import scrapy

class Programs_Spider(scrapy.Spider):
    name = "programs"

    start_urls = ['https://catalog.usf.edu/content.php?catoid=16&navoid=2287']

    def parse(self, response):
        self.logger.info('hello this is my first spider')
        pass