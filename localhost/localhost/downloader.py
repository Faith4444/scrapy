# -*- coding: utf-8 -*-
import time
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse, Response
import selenium.webdriver.support.ui as ui
from selenium import webdriver

class CustomDownloader(object):
    def __init__(self):
        # use any browser you wish
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.disk-cache"] = True
        cap["phantomjs.page.customHeaders.Cookie"] = ''
        self.browser = webdriver.PhantomJS(executable_path='C:/Python27/phantomjs/bin/phantomjs.exe', desired_capabilities=cap)

    def VisitPage(self, url):
        print '正在加载.....\n'.decode('utf-8').encode('gbk')
        self.browser.get(url)
        content = self.browser.page_source.encode('gbk', 'ignore')
        print '加载完毕.....\n'.decode('utf-8').encode('gbk')
        return content

    def __del__(self):
        self.browser.quit()
