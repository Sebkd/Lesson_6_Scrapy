import scrapy
from scrapy.http import HtmlResponse

from jobparser.items import JobparserItem


class SuperJobruSpider(scrapy.Spider):
    name = 'superjobru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=Python&geo%5Bt%5D%5B0%5D=4',
                  'https://www.superjob.ru/vacancy/search/?keywords=Python%20developer&geo%5Bt%5D%5B0%5D=4',
                  'https://www.superjob.ru/vacancy/search/?keywords=Python&payment_value=120000&'
                  'payment_defined=1&geo%5Bt%5D%5B0%5D=4&click_from=facet',
                  ]

    # custom_settings = {} можно каждого паука настроить индивидуально через этот атрибут

    def parse(self, response: HtmlResponse, **kwargs):

        next_page = response.xpath("//a[contains(@class, 'f-test-button-dalshe')]//span").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        SUPERJOB_LINK = 'https://www.superjob.ru'
        # response.css() - можно и через него искать
        links = response.xpath("//div[contains(@class, '_1O2dw')]//a/@href").getall()
        for link in links:
            link = SUPERJOB_LINK + link
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse, *args, **kwargs):
        name = response.xpath("//h1[contains(@class, 'KySx7')]/text()").get()
        salary = response.xpath("//span[contains(@class, '_2nJZK')]/span/text()").getall()
        url = response.url
        company = '---'
        yield JobparserItem(name=name, salary=salary, url=url, company=company)
