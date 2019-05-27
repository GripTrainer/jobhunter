import re
import yagmail

class JobAlertPipeline(object):
    def __init__(self, email, email_pass):
        self.email = email
        self.email_pass = email_pass
        self.keywords = re.compile('|'.join(['python', 'aws', ' r ']))
        self.jobs = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            email=crawler.settings['EMAIL'], 
            email_pass=crawler.settings['EMAIL_PASS']
        )

    def process_item(self, item, spider):
        if item.get('text') and self.keywords.search(item['text'].lower()):
            self.jobs.append(item)

        return item

    def close_spider(self, spider):
        mailer = yagmail.SMTP(self.email, self.email_pass)
        mailer.send(
            to=self.email,
            subject=f'Daily Job Hunt - {spider.name}', 
            contents=[field for job in self.jobs for field in (job.get('jobtitle'), job.get('url'))]
        )





