import scrapy


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&fromSearchLine=true&text=Python&from=suggest_post',
                  'https://hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&'
                  'search_field=description&salary=155000&only_with_salary=true&text=Python&from=suggest_post',]

    # custom_settings = {} можно каждого паука настроить индивидуально через этот атрибут

    def parse(self, response, **kwargs):
        print('current link:', response.url)
