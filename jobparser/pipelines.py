# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacancies0105

    def process_item(self, item, spider):

        if spider.name == 'hhru':
            item['company'] = ' '.join(item['company'])
            item['min_salary'], item['max_salary'], item['currency'], item['comment'] = self.process_salary(
                item['salary'])


            collection = self.mongobase[spider.name]
            collection.insert_one(item)

            return item

        if spider.name == 'superjob':
            item['company'] = ' '.join(item['company'])
            item['min_salary'], item['max_salary'], item['currency'], item['comment'] = self.process_salary_sj(
                item['salary'], item['url'])


            collection = self.mongobase[spider.name]
            collection.insert_one(item)

            return item

    def process_salary_sj(self, salary, url):
        FILL = '---'
        if len(salary) == 1:
            return FILL, FILL, FILL, salary[-1]
        if 'до' in salary:
            max_salary = salary[2] if salary[1] == ' ' else salary[1]
            if 'от' not in salary:
                min_salary = FILL
                comment = salary[-1]
                currency = 'руб.'
                return min_salary, max_salary, currency, comment
        elif 'от' in salary:
            min_salary = salary[2]
            if 'до' not in salary:
                max_salary = FILL
                comment = salary[-1]
                currency = 'руб.'
                return min_salary, max_salary, currency, comment
        else:
            min_salary = salary[0]
            max_salary = salary[1]
            currency = salary[-2]
            comment = salary[-1]
            return min_salary, max_salary, currency, comment

    def process_salary(self, salary):
        FILL = '---'
        if 'от ' not in salary and ' до ' not in salary and 'до ' not in salary:
            return FILL, FILL, FILL, ' '.join(salary)
        if 'от ' in salary:
            min_salary = salary[1]
        else:
            min_salary = FILL
        if ' до ' in salary:
            max_salary = salary[3]
        elif 'до ' in salary:
            max_salary = salary[1]
        else:
            max_salary = FILL
        if len(salary[-1]) > 4:
            currency = salary[-2]
            comment = salary[-1]
        else:
            currency = salary[-1]
            comment = FILL
        return min_salary, max_salary, currency, comment
