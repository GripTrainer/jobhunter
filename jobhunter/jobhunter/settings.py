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
# EMAIL = os.getenv('EMAIL')
# EMAIL_PASS = os.getenv('EMAIL_PASSWORD')

# S3
FEED_URI = 's3://jobhunter/%(name)s/%(time)s.json'
AWS_ACCESS_KEY_ID = os.getenv('KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('ACCESS_KEY')

# Pipelines 
# ITEM_PIPELINES = {
#     'jobhunter.pipelines.JobAlertPipeline': 300
# }
