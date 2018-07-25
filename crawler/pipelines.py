# -*- coding: utf-8 -*-
__author__ = 'MSteger'

from db.db import jobs, connect_and_create, record_exists, commit
from db.settings import MySQL_config

class CrawlerPipeline(object):
    def __init__(self):
        self.engine, self.session = connect_and_create(**MySQL_config)

    def process_item(self, item, *_):
        item['interesting'] = False
        if not record_exists(session=self.session, table=jobs, filter_logic={'title': item['title']}):
            entry = jobs(**item)
            commit(session=self.session, entry=entry)
        return item
