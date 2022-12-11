from crawler import HHCrawler, HabrCrawler
from parser import HHParser, HabrParser


if __name__ == "__main__":
    hh_crawler = HHCrawler()
    hh_vacancies_urls = hh_crawler.get_vacancies_urls(limit_per_specialization=1)
    print(hh_vacancies_urls)

    habr_crawler = HabrCrawler()
    habr_vacancies_urls = habr_crawler.get_vacancies_urls(limit=100)
    print(habr_vacancies_urls)

    for hh_vacancy_url in hh_vacancies_urls:
        hh_parser = HHParser(url=hh_vacancy_url, time_wait=0.0)
        hh_parser.parse()
        print(hh_parser.data)

    for habr_vacancy_url in habr_vacancies_urls:
        habr_parser = HabrParser(url=habr_vacancy_url)
        habr_parser.parse()
        print(habr_parser.data)
