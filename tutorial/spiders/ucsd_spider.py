import scrapy
import re
from tutorial.items import ProfessorItem


class ucsd(scrapy.Spider):
    name = "ucsd"
    start_urls = [
        "http://www.cse.ucsd.edu/faculty_profile#top",
    ]

    def parse(self, response):
    	for index in range(2,81):
    		str1=".//*[@id='faclist']/tbody/tr[%d]" % index
    		sel=response.xpath(str1)
        	item = ProfessorItem()
        	item['name']=sel.xpath("./td[2]/p/a/text()").extract()