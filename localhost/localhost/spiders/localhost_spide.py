#coding=utf-8
import time,re
from scrapy.item import Item, Field
from lxml import html
import urlparse
from scrapy.contrib.spiders import Spider
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from localhost.items import LocalhostItem
from bs4 import BeautifulSoup

class localhost (Spider):
    name='localhost'
    allowed_domains=['my_test_scrapy.com']
    start_urls = ['http://www.my_test_scrapy.com/ecshop/']
    old_urls =set()



    def parse(self, response):
        item=LocalhostItem()
        path=str(urlparse.urlparse(response.url).path)
        netname=str(urlparse.urlparse(response.url).netloc)
        scheme=str(urlparse.urlparse(response.url).scheme)
        self.old_urls.add(path)
        links=self.getLink(response.body,path)
        item['link']=response.url
        yield item

        for url in links:

            if self.checkUrl(url):

                url=scheme+'://'+netname+url
                print '----Request----:'+url
                yield Request(url, callback=self.parse)



    def getLink(self,html,path):
        rules=['href=[\'\"](.+?)[\'\"]',
                   'src=[\'\"](.+?)[\'\"]',
                   'img=[\'\"](.+?)[\'\"]',
                   'action=[\'\"](.+?)[\'\"]',
                   ]

        links=list()
        for rule in rules:
            link_iter = re.finditer(rule, html,re.S)
            for link in link_iter:
                result= self.fiterUrl(link.group(1),path)
                links.append(urlparse.urljoin(path,result))
        links=list(set(links))
        return links

    def checkUrl(self,url):
        if url in self.old_urls:
            return False
        else:
            return True

    def fiterUrl(self,url,path):
        rule1 = '(.+)/(.+)((\.js)|(\.gif)|(\.png)|(\.ico)|(\.bmp)|(\.css)|(\.jpg)|(\.lbi)|(\.mno)|(\.dwt))$'
        rule2='(.+?)((\.js)|(\.gif)|(\.png)|(\.ico)|(\.bmp)|(\.css)|(\.jpg)|(\.lbi)|(\.mno)|(\.dwt))$'
        Pattern1= re.compile(rule1, re.S)
        Pattern2 = re.compile(rule2, re.S)
        rs1=re.search(Pattern1,url)
        rs2 = re.search(Pattern2, url)
        if rs1:
            return str(rs1.group(1))
        elif rs2:
            return ""
        elif 'http'in url or 'https' in url:
            return ""
        else:
            return url
'''
    def parse_form(self,html):
        rule1 = '<form.+?method="get".+?>(.+?)</form>'

'''



