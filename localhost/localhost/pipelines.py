# -*- coding: utf-8 -*-
import json
import codecs
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LocalhostPipeline(object):
    def __init__(self):
        self.file = open('ecshop_url_txt','w')

    def process_item(self, item, spider):
        self.file.write(item['link']+'\n')
        return item
