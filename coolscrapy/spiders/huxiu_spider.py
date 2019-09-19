from coolscrapy.items import HuxiuItem
import scrapy
from scrapy.shell import inspect_response

class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_urls = [
        "http://www.huxiu.com/index.php"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()
            item['title'] = sel.xpath('h2/a/text()')[0].extract()
            item['link'] = sel.xpath('h2/a/@href')[0].extract()
            url = response.urljoin(item['link'])
            item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
            # print(item['title'],item['link'],item['desc'])
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="article-wrapper"]')
        #inspect_response(response, self)
        item = HuxiuItem()
        item['title'] = detail.xpath('div/section/div/div[1]/div[1]/h1/text()')[0].extract()
        item['link'] = response.url
        item['posttime'] = detail.xpath('div/section/div/div[1]/div[1]/span/text()')[0].extract()
        print(item['title'],item['link'],item['posttime'])
        yield item
