import pytz
from scrapy.spiders import SitemapSpider
from jobhunter.itemloaders import JobAdloader
from jobhunter.items import JobAd
from datetime import datetime, timedelta


class TrademeSpider(SitemapSpider):
    name = 'trademe'
    allowed_domains = ['trademe.co.nz']
    sitemap_urls = ['https://www.trademe.co.nz/sitemaps/Trade-Me-Jobs.xml']
    sitemap_follow = ['-Jobs-IT-']
    sitemap_rules = [('/jobs', 'parse_job')]

    def __init__(self):
        self.tz = pytz.timezone('NZ')

    def sitemap_filter(self, entries):
        for entry in entries:
            date_time = datetime.strptime(entry['lastmod'], '%Y-%m-%dT%H:%M:%SZ')
            date_time = date_time.replace(tzinfo=self.tz)
            if date_time > datetime.now(self.tz) - timedelta(days=1):
                yield entry

    def parse_job(self, response):
        jl = JobAdloader(item=JobAd(), response=response)
        jl.add_value('id', response.text, re='"listingId": (\d+)')
        jl.add_value('jobtitle', response.text, re='"title": "([^"]+)"')
        jl.add_css('classification', '#jobs-breadcrumb-depth-2::text')
        jl.add_value('listingdate', response.text, re=r'\w{3} \d{1,2} \w{3}, \d{1,2}:\d\d \w{2}')
        jl.add_css('expirydate', '#JSocialTools_JExpireTimeLabel::text')
        jl.add_value('company', response.text, re='"jobsCompany": "([^"]+)"')
        jl.add_css('text', '#j-description-contents *::text')
        jl.add_value('url', response.url)
        yield jl.load_item()

