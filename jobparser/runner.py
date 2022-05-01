from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from jobparser import settings
from jobparser.spiders.hhru import HhruSpider
from jobparser.spiders.superjob import SuperjobSpider

if __name__ == '__main__':  # ctrl+j main

    configure_logging()

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    runner = CrawlerRunner(settings=crawler_settings)
    runner.crawl(SuperjobSpider)
    runner.crawl(HhruSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()

    # process_ = CrawlerProcess(settings=crawler_settings)
    # process_.crawl(SuperjobSpider)
    #
    # process_.crawl(HhruSpider)
    # process_.start()

