from abs import ABS
import os
import requests

class GetAPI(ABS):
    def unit(self):
        pass





class HeadHunterAPI(GetAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/'
        self.params = {'count': 5, 'town': 'Moscow'}

    def unit(self):
        response =requests.get(self.url, headers={'User-Agent': 'MyApp/1.0 (crazyanimalcz@gmail.com)'})
        return response

class SuperJobAPI(GetAPI):
    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        # self.headers = {'X-Api-App-Id': os.getenv('SJ_API')}
        self.params = {'count': 5, 'town': 'Moscow'}

    def unit(self):
        response =requests.get(self.url, headers={'X-Api-App-Id': os.getenv('SJ_API')})
        data = response.json()
        return data

super_job = HeadHunterAPI()
print(super_job.unit())