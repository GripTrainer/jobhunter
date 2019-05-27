import os
from dotenv import load_dotenv

load_dotenv()

BOT_NAME = 'jobhunter'

SPIDER_MODULES = ['jobhunter.spiders']
NEWSPIDER_MODULE = 'jobhunter.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Mail Settings
EMAIL = os.getenv('EMAIL')
EMAIL_PASS = os.getenv('EMAIL_PASSWORD')

# Pipelines 
ITEM_PIPELINES = {
    'jobhunter.pipelines.JobAlertPipeline': 300
}

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
