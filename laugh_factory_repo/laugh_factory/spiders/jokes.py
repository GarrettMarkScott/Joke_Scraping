import scrapy

class JokesSpider(scrapy.Spider):
    name = 'jokes'

    start_urls = [
        'http://www.laughfactory.com/jokes/office-jokes'
    ]

    def parse(self, response):
        for joke in response.xpath('//div[@class="jokes"]'):
            yield {
            'joke_text': joke.xpath('.//div[@class="joke-text"]/p').extract_first()
            }
#Note that the period in the 'joke_text' serves the purpose of keeping it to just the response element

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

#Terminal: scrapy crawl jokes -o data.json
