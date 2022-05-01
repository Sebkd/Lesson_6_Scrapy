from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from jobparser import settings
from jobparser.spiders.hhru import HhruSpider
from jobparser.spiders.superjob import SuperjobSpider

if __name__ == '__main__':  # ctrl+j main
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process_ = CrawlerProcess(settings=crawler_settings)
    process_.crawl(SuperjobSpider)
    process_.start()


    # process_.stop()

    # process_.crawl(HhruSpider)
    # process_.start()

    # d = process_.join()
    # d.addBoth(lambda _: reactor.stop())
    # reactor.run()

    # process_.start()
