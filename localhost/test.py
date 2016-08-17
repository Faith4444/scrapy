#coding=utf-8
from selenium import webdriver
import os,re
class CustomDownloader(object):
    def __init__(self):
        # use any browser you wish
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.disk-cache"] = True
        self.browser = webdriver.PhantomJS(executable_path='C:/Python27/phantomjs/bin/phantomjs.exe', desired_capabilities=cap)

    def VisitPage(self, url):
        print '正在加载.....\n'.decode('utf-8').encode('gbk')
        self.browser.get(url)
        content = self.browser.page_source.encode('gbk', 'ignore')
        print '加载完毕.....\n'.decode('utf-8').encode('gbk')
        return content

    def __del__(self):
        self.browser.quit()
'''


url='http://www.my_test_scrapy.com/1.html'
content = weki.VisitPage(url)
print content
'''

html='''
    <form id="searchForm" name="searchForm" method="get" action="search.php" onSubmit="return checkSearchForm()" class="f_r">
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="135"><input name="keywords" type="text" id="keyword" value="" class="B_input"  />
            <input name="keyword222" type="text" id="keyword11" value="" class="B_input"  /></td>
            <td><input name="imageField" type="submit" value="搜索" class="go" style="cursor:pointer;" /></td>
          </tr>
        </table>
      </form>
'''


weki=CustomDownloader()

def parse_form(html):
    rule1 = '<form.+?method="get".+?>.+?</form>'
    Pattern1 = re.compile(rule1, re.S)
    rs = re.search(Pattern1, html)
    if rs:
        rule2 = '<input.*?name="(.*?)".*?type="text".*?/>'
        Pattern2 = re.compile(rule2, re.S)
        inputs_name = re.findall(Pattern2, html)
        for name in inputs_name:



print parse_form(html)












