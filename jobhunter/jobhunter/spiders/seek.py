import scrapy
import re

from jobhunter.itemloaders import SeekLoader
from jobhunter.items import JobAd

BASE_URL = 'https://www.seek.co.nz'

class SeekSpider(scrapy.Spider):
    name = 'seek'
    start_urls = [
        f'{BASE_URL}/jobs-in-information-communication-technology/in-All-Wellington?sortmode=ListedDate'
    ]

    def parse(self, response):
        for job in response.css('a[href*="/job/"]'):
            yield response.follow(job, callback=self.parse_job)

        for page in response.css('p span a'):
            yield response.follow(page)
        

    def parse_job(self, response):
        sl = SeekLoader(item=JobAd(), response=response)
        sl.add_value('id', response.text, re=r'"id":(\d+)')
        sl.add_value('classification', response.text, re=r'"jobSubClassification":"([^"]+)')
        sl.add_value('listingdate', response.text, re=r'"listingDate":"([^"]+)"')
        sl.add_value('expirydate', response.text, re=r'"expiryDate":"([^"]+)"')
        sl.add_value('company', response.text, re=r'"advertiserName":"([^"]+)"')
        sl.add_css('jobtitle', 'h1.jobtitle::text')
        sl.add_css('text', '.templatetext ::text')
        yield sl.load_item()