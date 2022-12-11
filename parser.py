import json
import requests
import time

from bs4 import BeautifulSoup

from headers_generation import get_headers


class Parser:
    def __init__(self, url: str, time_wait: float = 0.5):
        self.time_wait = time_wait
        self.url = url
        self.data = {}

    def parse(self):
        time.sleep(self.time_wait)

        rq = requests.get(self.url, headers=get_headers())
        print('Getting HTML-code from ', self.url)

        if rq.status_code != 200:
            print(f'Error {rq.status_code}: {self.url}')
            return

        self._get_vacancy_id(rq.text)
        self._task_1(rq.text)
        self._task_2(rq.text)

    def _get_vacancy_id(self, html: str):
        pass

    def _task_1(self, html: str):
        pass

    def _task_2(self, html: str):
        pass


class HHParser(Parser):
    def _get_vacancy_id(self, html: str):
        data_dict = json.loads(html)
        self.data['id'] = data_dict['id']
        self.data['source'] = 'https://hh.ru'

    def _task_1(self, html: str):
        pass

    def _task_2(self, html: str):
        pass


class HabrParser(Parser):
    def _get_vacancy_id(self, html: str):
        html_bs = BeautifulSoup(html, features='html.parser')
        data_dict = json.loads(html_bs.find('script', type='application/json').text)
        self.data['id'] = data_dict['vacancy']['id']
        self.data['source'] = 'https://career.habr.com'

    def _task_1(self, html: str):
        pass

    def _task_2(self, html: str):
        pass
