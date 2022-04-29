# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JobparserPipeline:
    def process_item(self, item, spider):
        item['company'] = ' '.join(item['company'])
        item['min_salary'], item['max_salary'], item['currency'] = self.process_salary(item['salary'])
        return item



    def process_salary(self, salary):
        if 'от ' not in salary and ' до ' not in salary:
            return '0', '0', '---'
        if 'от ' in salary:
            min_salary = salary[1]
        else:
            min_salary = ''
        if ' до ' in salary:
            max_salary = salary[3]
        else:
            max_salary = ''
        if len(salary[-1]) > 4:
            currency = salary[-2]
        else:
            currency = salary[-1]
        print()
        return min_salary, max_salary, currency