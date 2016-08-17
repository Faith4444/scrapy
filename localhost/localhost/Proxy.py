#coding=utf-8
import random
class Proxy(object):
    def __init__(self,path):
        self.path=path
        self.proxys=list()
        self.get_proxy()

    def get_proxy(self):
        f=open(self.path)
        while 1:
            line=f.readline()
            self.proxys.append(line)
            if not line:
                break

    def choice_proxy(self):
        return random.choice(self.proxys)


if __name__=='__main__':
    p=Proxy('proxy.txt')
    print p.choice_proxy()