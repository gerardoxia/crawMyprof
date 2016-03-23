'''import scrapy
from tutorial.items import ProfessorItem


class upenn(scrapy.Spider):
    name = "upenn"
    start_urls = [
        "http://www.cis.upenn.edu/about-people/index.php",
    ]


    def parse(self, response):
        for index in range(2,41,2):
        	str1=".//*[@id='Left']/table/tr[%d]" % index
        	sel=response.xpath(str1)
        	item = ProfessorItem()
        	if(sel.re(r"Research Area")):item['area']=sel.re(r"Area.*?</strong>(.*?)<br>")[0]
        	if(sel.re(r"Name:</strong>(.*?), ")):
        		item['name']=sel.re(r"Name:</strong>(.*?), ")[0]
        		item['title']=sel.re(r"Name:</strong>(.*?), (.*)<br>")[1]
        	else:
        		item['name']=sel.re(r"Name: </strong>(.*?), ")[0]
        		item['title']=sel.re(r"Name: </strong>(.*?), (.*)<br>")[1]
        	item['img']="http://www.cis.upenn.edu"+sel.css("td >img::attr('src')").re(r"..(.*)")[0]
        for index in range(43,54,2):
        	str1=".//*[@id='Left']/table/tr[%d]" % index
        	sel=response.xpath(str1)
        	item = ProfessorItem()
        	if(sel.re(r"Area")):item['area']=sel.re(r"Area.*?</strong>(.*?)<br>")[0]
        	item['name']=sel.re(r"Name:</strong>(.*?), ")[0]
        	item['title']=sel.re(r"Name:</strong>(.*?), (.*)<br>")[1]
        	item['img']="http://www.cis.upenn.edu"+sel.css("td >img::attr('src')").re(r"..(.*)")[0]
        	yield item
        for index in range(56,87,2):
        	str1=".//*[@id='Left']/table/tr[%d]" % index
        	sel=response.xpath(str1)
        	item = ProfessorItem()
        	if(sel.re(r"Area")):item['area']=sel.re(r"Area.*?</strong>(.*?)<br>")[0]
        	item['name']=sel.re(r"Name:</strong>(.*?), ")[0]
        	item['title']=sel.re(r"Name:</strong>(.*?), (.*)<br>")[1]
        	item['img']="http://www.cis.upenn.edu"+sel.css("td >img::attr('src')").re(r"..(.*)")[0]
        	yield item'''