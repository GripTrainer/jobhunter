from scrapy.spiders import SitemapSpider
from jobhunter.itemloaders import TrademeLoader
from jobhunter.items import JobAd


class TrademeSpider(SitemapSpider):
    name = 'trademe'
    allowed_domains = ['trademe.co.nz']
    sitemap_urls = ['https://www.trademe.co.nz/sitemaps/Trade-Me-Jobs.xml']
    sitemap_follow = ['-Jobs-IT-']
    sitemap_rules = [('/jobs', 'parse_job')]

    def parse_job(self, response):
        tl = TrademeLoader(item=JobAd(), response=response)
        tl.add_value('id', response.text, re='"listingId": (\d+)')
        tl.add_value('jobtitle', response.text, re='"title": "([^"]+)"')
        tl.add_css('classification', '#jobs-breadcrumb-depth-2::text')
        tl.add_value('listingdate', response.text, re=r'\w{3} \d{1,2} \w{3}, \d{1,2}:\d\d \w{2}')
        tl.add_css('expirydate', '#JSocialTools_JExpireTimeLabel::text')
        tl.add_value('company', response.text, re='"jobsCompany": "([^"]+)"')
        tl.add_css('text', '#j-description-contents *::text')
        yield tl.load_item()

