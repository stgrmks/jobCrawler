#-*- coding: UTF-8 -*-
__author__ = 'MSteger'

from scrapy.spiders import Spider
from scrapy.http import Request
from ..items import jobItem
from settings import StepStone_config

class StepStone(Spider):

    name = 'StepStone'
    job_title = StepStone_config['job_title']
    location = StepStone_config['location']
    radius = StepStone_config['radius']
    jobs_per_page = StepStone_config['jobs_per_page']
    allowed_domains = ['www.stepstone.de']
    startPage = StepStone_config['startPage']
    maxPages = StepStone_config['maxPages']
    url = 'https://www.stepstone.de/5/ergebnisliste.html?ke={}&ws={}&ra={}&li={}&suid=2c0c263d-efde-4d1c-92e1-5915c934b60c'.format(job_title, location, radius, jobs_per_page)

    def start_requests(self, numberOfPage = 0):
        search_url = '{}&of={}00'.format(self.url, numberOfPage)
        req = Request(url=search_url, callback=self.parse)
        req.meta['numberOfPage'] = numberOfPage
        return [req]

    def parse(self, response):
        num = response.meta['numberOfPage']
        jobs = response.css('article')

        for job in jobs:
            item = jobItem()
            item['title'] = job.xpath('.//div[@class="job-element__body word-wrap"]/a/h2/text()').extract()[0]
            item['company'] = job.xpath('.//div[@class="job-element__body__company"]/text()').extract()[0]
            item['date'] = job.xpath('.//div[@class="job-element__body word-wrap"]/ul/li[1]/time/@data-date').extract()[0]
            item['location'] = ' '.join(job.xpath('.//div[@class="job-element__body word-wrap"]/ul/li[2]/text()').extract())
            item['link'] = job.xpath('.//div[@class="job-element__body word-wrap"]/a/@href').extract()[0]
            yield item

        if num > self.maxPages: return

        yield self.start_requests(num+1)[0]




if __name__== '__main__':
    print 'done'

