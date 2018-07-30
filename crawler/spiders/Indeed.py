#-*- coding: UTF-8 -*-
__author__ = 'MSteger'

from scrapy.spiders import Spider
from scrapy.http import Request
from ..items import jobItem
from settings import Indeed_config

class Indeed(Spider):

    name = 'Indeed'
    job_title = Indeed_config['job_title']
    location = Indeed_config['location']
    radius = Indeed_config['radius']
    jobs_per_page = Indeed_config['jobs_per_page']
    allowed_domains = ['www.indeed.de', 'www.indeed.com']
    startPage = Indeed_config['startPage']
    maxPages = Indeed_config['maxPages']
    url = 'https://de.indeed.com/Jobs?q={}&l={}&radius={}&limit={}'.format(job_title, location, radius, jobs_per_page)

    def start_requests(self, numberOfPage = 0):
        search_url = '{}&start={}00'.format(self.url, numberOfPage*self.jobs_per_page)
        req = Request(url=search_url, callback=self.parse)
        req.meta['numberOfPage'] = numberOfPage
        return [req]

    def parse(self, response):
        num = response.meta['numberOfPage']
        jobs = response.css('//td[@id="resultsCol"]')

#//*[@id="pj_c8df832c901a4471"] //*[@id="resultsCol"]/div[5]
        for job in jobs:
            item = jobItem()
            item['title'] = job.xpath('.//div[@class="job-element__body word-wrap"]/a/h2/text()').extract()[0]
            item['company'] = job.xpath('.//div[@class="job-element__body__company"]/text()').extract()[0]
            item['date'] = job.xpath('.//div[@class="job-element__body word-wrap"]/ul/li[1]/time/@data-date').extract()[0]
            item['location'] = ' '.join(job.xpath('.//div[@class="job-element__body word-wrap"]/ul/li[2]/text()').extract())
            item['link'] = job.xpath('.//div[@class="job-element__body word-wrap"]/a/@href').extract()[0]
            item['source'] = 'Indeed'
            print 'test'

        #     yield item
        #
        # if num > self.maxPages: return
        #
        # yield self.start_requests(num+1)[0]




if __name__== '__main__':
    print 'done'

