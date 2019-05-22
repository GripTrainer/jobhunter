import scrapy

class SeekItem(scrapy.Item):
    id = scrapy.Field()
    jobtitle = scrapy.Field()
    classification = scrapy.Field()
    listingdate = scrapy.Field()
    expirydate = scrapy.Field()
    company = scrapy.Field()
    text = scrapy.Field()