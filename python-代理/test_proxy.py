#coding=utf-8
import time
import requests
import threading

inFile = open('proxy.txt', 'r')
outFile = open('available.txt', 'w')
lock = threading.Lock()

def test():
    while True:
        lock.acquire()
        line = inFile.readline().strip()
        lock.release()
        if len(line) == 0:
            break
        proxy_info = line.split('||')[0]
        try:
            proxies = {
                "http": "http://%s"%proxy_info,
            }
            respone=requests.get("http://www.tsinghua.edu.cn/publish/newthu/index.html", proxies=proxies, timeout=10)
            if  'publish/newthu/images/favicon.ico' in respone.text:
                lock.acquire()
                print 'add proxy:%s\n'%proxy_info
                outFile.write(proxy_info + '\n')
                lock.release()

        except Exception, e:
            print "Fail proxy:%s\n" % proxy_info




all_thread = []
for i in range(500):
    t = threading.Thread(target=test)
    all_thread.append(t)
    t.start()

for t in all_thread:
    t.join()

inFile.close()
outFile.close()
