from abc import ABC
import os
import requests


class GetAPI(ABC):
    def __init__(self, name, page, top_n):
        self.name = name
        self.page = page
        self.top_n = top_n

    def get_vacancies(self):
        pass


class HeadHunterAPI(GetAPI):
    def __init__(self, name, page, top_n):
        super().__init__(name, page, top_n)
        self.url = 'https://api.hh.ru/'

    def get_vacancies(self):
        """Выгрузка данных по 'HH' по запросам пользователя и возвращается словарь"""

        data = requests.get(f'{self.url}/vacancies',
                            params={'text': self.name, 'page': self.page, 'per_page': self.top_n}).json()
        return data


class SuperJobAPI(GetAPI):
    def __init__(self, name, page, top_n):
        super().__init__(name, page, top_n)
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.params = {'count': 5, 'town': 'Moscow'}

    def get_vacancies(self):
        response = requests.get(self.url, headers={'X-Api-App-Id': os.getenv('SJ_API')})
        data = response.json()
        return data


super_job = HeadHunterAPI()

