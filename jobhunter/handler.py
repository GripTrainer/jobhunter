import scrapydo
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from jobhunter.spiders.seek import SeekSpider
from jobhunter.spiders.indeed import IndeedSpider
from jobhunter.spiders.trademe import TrademeSpider

spider_dictionary = {
    'seek': SeekSpider,
    'indeed': IndeedSpider,
    'trademe': TrademeSpider
}


def jobhunt(event, context):
    scrapydo.setup()
    settings = get_project_settings()
    scrapydo.run_spider(spider_dictionary[event['name']], settings=settings)


if __name__ == '__main__':
    jobhunt({'name': 'seek'}, {})
