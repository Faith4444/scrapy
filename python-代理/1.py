#coding=utf8

import requests
import time
proxies = {
    "http": "http://121.193.143.249:80",
}


try:
    start = time.time()
    r=requests.get("http://www.tsinghua.edu.cn/publish/newthu/index.html", proxies=proxies)
    if 'favicon.ico' in r.text:
        print 1111111
except:
    print 2222

end = time.time()
print "time:%s" % (end - start)
