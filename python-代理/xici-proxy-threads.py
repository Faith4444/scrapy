#coding=utf-8
import Queue
import threading
import re
import urllib2
import downloader as downloader
import time

lock = threading.Lock()
of=open('proxy.txt','w')
weki = downloader.CustomDownloader()

class WorkManager(object):
    def __init__(self,work_page,thread_num):
        self.work_queue=Queue.Queue()
        self.threads=[]
        work_page=self.all_page_url(work_page)
        self.init_work_queue(work_page)
        self.init_thread_pool(thread_num)

    def init_work_queue(self,work_page):
        for page in work_page:
            self.work_queue.put((get_proxy,page))

    def init_thread_pool(self,thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))

    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()

    def all_page_url(self,workpage):
        all_page=['http://www.xicidaili.com/nn/'+str(x) for x in range(1,workpage+1)]
        return all_page


class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        while True:
            try:
                do, args = self.work_queue.get(block=False)
                do(args)
                self.work_queue.task_done()
            except:
                break

def get_proxy(page_url):
    url = page_url
    respone = weki.VisitPage(url)
    rule1 = "<tr.*?>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>([\s\S]*?) </td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>"
    pattern1 = re.compile(rule1, re.S)
    results = re.findall(pattern1, respone)
    for iters in results:
        iters = list(iters)
        iters = [iter.strip() for iter in iters]

        if 'a' in iters[2]:
            rule2 = '<a.*?>(.*?)</a>'
            pattern2 = re.compile(rule2, re.S)
            s = re.match(pattern2, iters[2])
            iters[2] = s.group(1)
            print "%s:%s||%s||%s||%s\n" % (iters[0], iters[1], iters[2], iters[4], iters[5])
        else:
            print "%s:%s||%s||%s||%s\n" % (iters[0], iters[1], iters[2], iters[4], iters[5])
        lock.acquire()
        of.write("%s:%s||%s||%s||%s\n" % (iters[0], iters[1], iters[2], iters[4], iters[5]))
        lock.release()

if __name__ == '__main__':
    start = time.time()
    work_manager=WorkManager(50,50)
    work_manager.wait_allcomplete()
    end = time.time()
    print "time:%s"%(end-start)