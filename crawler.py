import json
import requests
import time

from headers_generation import get_headers


def get_html(url: str) -> str:
    rq = requests.get(url, headers=get_headers())
    print('Getting HTML-code from ', url)
    return rq.text


def is_empty(html: str, vacancy_list_attribute: str) -> bool:
    data_dict = json.loads(html)

    if not data_dict.get(vacancy_list_attribute):
        return True

    return False


def get_offers_links(html, vacancy_list_attribute: str, url_attribute: str):
    links = []

    data_dict = json.loads(html)
    vacancy = data_dict[vacancy_list_attribute]

    for item in vacancy:
        links.append(item[url_attribute])
    return links


class HabrCrawler:
    def __init__(self, query: str = '', areas: list = None, per_page: int = 100, specializations: list = None,
                 time_wait: float = 0.5):
        self.query = query
        self.per_page = per_page
        self.areas = areas
        self.specializations = specializations
        self.root_url = 'https://career.habr.com/api/frontend/vacancies?'
        self.time_wait = time_wait

    def get_vacancies_urls(self, limit: int = None):
        all_links = []
        page = 0

        vacancy_root_url = 'https://career.habr.com'

        while True:
            url = f"{self.root_url}page={page}&per_page={self.per_page}"
            if self.areas:
                for area in self.areas:
                    url += f"&area={area}"
            if self.specializations:
                for specialization in self.specializations:
                    pass
            time.sleep(self.time_wait)
            html = get_html(url)
            if is_empty(html, vacancy_list_attribute='list'):
                break

            all_links += [f"{vacancy_root_url}{x}" for x in get_offers_links(html,
                                                                             vacancy_list_attribute='list',
                                                                             url_attribute='href')]
            page += 1

            if len(all_links) > limit:
                all_links = all_links[:limit]
                break

        return list(set(all_links))


class HHCrawler:
    def __init__(self, query: str = '', areas: list = None, per_page: int = 100, specializations: list = None,
                 time_wait: float = 0.0):
        self.query = query

        if areas is None:
            self.areas = [113]

        self.per_page = per_page

        if specializations is None:
            self.specializations = [160,
                                    10,
                                    12,
                                    150,
                                    25,
                                    165,
                                    34,
                                    36,
                                    73,
                                    155,
                                    96,
                                    164,
                                    104,
                                    157,
                                    107,
                                    112,
                                    113,
                                    148,
                                    114,
                                    116,
                                    121,
                                    124,
                                    125,
                                    126]

            self.root_url = 'https://api.hh.ru/vacancies?'
            self.time_wait = time_wait

    def get_vacancies_urls(self, limit_per_specialization: int = None):
        all_links = []

        for specialization in self.specializations:
            page = 0

            links_to_add = []

            while True:
                url = f"{self.root_url}text={self.query}&page={page}&per_page={self.per_page}" \
                      f"&professional_role={specialization}"
                for area in self.areas:
                    url += f"&area={area}"
                time.sleep(self.time_wait)
                html = get_html(url)
                if is_empty(html, vacancy_list_attribute='items'):
                    break

                links_to_add += get_offers_links(html, vacancy_list_attribute='items', url_attribute='url')
                page += 1

                if len(links_to_add) > limit_per_specialization:
                    links_to_add = links_to_add[:limit_per_specialization]
                    break

            all_links.extend(links_to_add)

        return list(set(all_links))
