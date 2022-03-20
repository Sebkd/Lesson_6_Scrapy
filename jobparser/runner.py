from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Lesson_6_Scrapy.jobparser import settings
from Lesson_6_Scrapy.jobparser.spiders.hhru import HhruSpider

if __name__ == '__main__':  # ctrl+j main
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider)

    process.start()
