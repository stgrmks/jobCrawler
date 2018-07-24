__author__ = 'MSteger'

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__== '__main__':
    bot = CrawlerProcess(get_project_settings())
    bot.crawl('StepStone')
    bot.start()
    print 'done'