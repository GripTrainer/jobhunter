BOT_NAME = 'jobhunter'

SPIDER_MODULES = ['jobhunter.spiders']
NEWSPIDER_MODULE = 'jobhunter.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
