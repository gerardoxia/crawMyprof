import scrapy
from tutorial.items import ProfessorItem


class princeton(scrapy.Spider):
    name = "princeton"
    start_urls = [
        "https://www.cs.princeton.edu/people/faculty",
    ]

    def parse(self, response):
        for sel in response.xpath(".//*[@id='block-system-main']/div/div[2]/div"):
            item = ProfessorItem()
            if(sel.xpath('./div[2]/h2/a/text()[1]')):
                item['name'] = sel.xpath('./div[2]/h2/a/text()[1]').extract()[0].strip()
            else: item['name'] = sel.xpath('./div[2]/h2/text()[1]').extract()[0].strip()
            item['title'] = sel.xpath('./div[2]/div[1]/text()[1]').extract()[0].strip()
            item['edu'] = sel.xpath('./div[2]/div[2]/text()[1]').extract()[0].strip()
            item['email'] = sel.xpath('./div[2]/div[4]/span[1]/text()[2]').extract()[0]
            #item['phone'] = sel.xpath('./div[2]/div[4]/span[2]/text()[1]').extract()[0]
            #item['addr'] = sel.xpath('./div[2]/div[4]/span[3]/text()[1]').extract()[0]
            #item['url'] = sel.css(".views-field-field-person-photo .field-content a::attr('href')").extract()[0]
            item['img'] = sel.css(".person-photo img::attr('src')").extract()[0]
            #item['area'] = ", ".join(sel.css('.views-field-term-node-tid .field-content > a::text').extract()).replace(u', and', u',')
            yield item