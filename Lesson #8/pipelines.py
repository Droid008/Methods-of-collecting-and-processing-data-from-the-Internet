# -*- coding: utf-8 -*-
from pymongo import MongoClient

class InstaparserPipeline:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.mongo_base = self.client.instagram

    def process_item(self, item, spider):
        if spider.name == 'instagram':
            collection = self.mongo_base['subscriptions']
            collection.insert_one(item)
        elif spider.name == 'instagram_subscribers':
            collection = self.mongo_base['subscribers']
            collection.insert_one(item)
        return item

    def __del__(self):
        self.client.close()