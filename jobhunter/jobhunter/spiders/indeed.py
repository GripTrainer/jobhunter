import scrapy
from jobhunter.items import JobAd
from jobhunter.itemloaders import JobAdloader

class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    start_urls = ['https://nz.indeed.com/jobs?l=Wellington&sort=date&fromage=1']

    def parse(self, response):
        for job in response.css('.title a'):
            yield response.follow(job, callback=self.parse_job)
        
        for page in response.css('.pagination a'):
            yield response.follow(page)

    def parse_job(self, response):
        jl = JobAdloader(item=JobAd(), response=response)
        jl.add_value('id', response.url, re=r'jk=([^&]+)')
        jl.add_value('jobtitle', response.text, re=r'"jobTitle":"([^"]+)"')
        jl.add_css('company', '.icl-u-xs-mr--xs::text')
        jl.add_css('text', '.jobsearch-jobDescriptionText *::text')
        yield jl.load_item()
        
    