import requests

from src.exceptions import EmptyList
from src.parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'area': 113}
        self.vacancies = []

    def load_vacancies(self, job_vacancy: str):
        """
        Метод для получения списка вакансий
        :param job_vacancy: наименование вакансии
        :return: список вакансий
        """
        self.params['text'] = job_vacancy
        while self.params.get('page') != 3:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    def get_vacancies(self, vacancy_to_search: str) -> list:
        """
        Метод возвращает список вакансий
        :param vacancy_to_search: вакансия для поиска
        :return: список вакансий
        """
        self.load_vacancies(vacancy_to_search)
        if self.vacancies:
            return self.vacancies
        raise EmptyList('Поиск не дал результата. \nПредлагаю начать всё заново:)')
