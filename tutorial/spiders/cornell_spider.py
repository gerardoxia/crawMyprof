import scrapy
from tutorial.items import ProfessorItem


class cornell(scrapy.Spider):
    name = "cornell"
    start_urls = [
        "https://www.cs.cornell.edu/people/faculty",
    ]

    def parse(self, response):
        for sel in response.xpath(".//*[@id='node-93']/div/div/div/div/div/div"):
            item = ProfessorItem()
            item['name'] = sel.css("a > img::attr('alt')").extract()[0]
            item['title'] = sel.xpath('./div/p[1]/text()').extract()[0].strip()
            '''item['addr'] = selContent.xpath('./text()[2]').extract()[0].strip()
            item['email'] = selContent.xpath('./a/text()').extract_first()
            item['phone'] = selContent.xpath('./text()[4]').extract()[0].strip()
            item['url'] = ", ".join(selContent.css("a:nth-of-type(3)::attr('href')").extract())'''
            item['img'] = "https://www.cs.cornell.edu"+sel.css("a > img::attr('src')").extract()[0]
            #item['area'] = ", ".join(sel.css('.views-field-field-research .item-list > ul > li > a::text').extract()).replace(u', and', u',')
            yield item