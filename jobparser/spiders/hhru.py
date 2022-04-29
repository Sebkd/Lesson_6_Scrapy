import scrapy
from scrapy.http import HtmlResponse

from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?clusters=true&area=1&ored_clusters=true&enable_snippets=true&salary'
                  '=&text=Python',
                  'https://hh.ru/search/vacancy?area=1&fromSearchLine=true&text=Python+junior&from=suggest_post',
                  'https://hh.ru/search/vacancy?area=1&experience='
                  'noExperience&search_field=name&search_field=company_name&search_field=description&'
                  'text=Python&clusters=true&ored_clusters=true&enable_snippets=true',
                  ]

    # custom_settings = {} можно каждого паука настроить индивидуально через этот атрибут

    def parse(self, response: HtmlResponse, **kwargs):

        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        # response.css() - можно и через него искать
        links = response.xpath("//a[@data-qa='vacancy-serp__vacancy-title']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse, *args, **kwargs):
        name = response.xpath("//h1//text()").get()
        salary = response.xpath("//span[contains(@data-qa, 'vacancy-salary')]/text()").getall()
        url = response.url
        company = response.xpath("//div[contains(@data-qa, 'vacancy-company__details')]//text()").getall()
        yield JobparserItem(name=name, salary=salary, url=url, company=company)
