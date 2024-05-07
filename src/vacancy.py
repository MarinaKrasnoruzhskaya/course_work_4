import re
from datetime import datetime


class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, vacancy_id: str, name: str, url: str, published_at: str, salary: dict, snippet: str):
        self.id = vacancy_id
        self.name = name
        self.url = url
        self.published_at = published_at
        self.salary = {
            'from': self.validate_salaries(salary['from']),
            'to': self.validate_salaries(salary['to']),
            'currency': salary['currency']
        } if salary else {'from': 0, 'to': 0, 'currency': ''}
        self.snippet = re.sub(r'<.*?>', '', snippet) if snippet else ''

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Наименование: {self.name}\n"
                f"URL: {self.url}\n"
                # f"Опубликовано: {self.published_at}\n"
                f"Опубликовано: {datetime.strptime(self.published_at, "%Y-%m-%dT%H:%M:%S%z").date()}\n"
                f"Зарплата: {self.get_str_salary()}\n"
                f"Требования: {self.snippet}\n")

    def __ge__(self, other) -> bool:
        """ Метод для оператора >= """
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")

        sc = other if isinstance(other, int) else other.salary['from']

        if self.salary['from'] and self.salary['to']:
            return self.salary['from'] >= sc and self.salary['to'] >= sc
        elif self.salary['from']:
            return self.salary['from'] >= sc
        elif self.salary['to']:
            return self.salary['to'] >= sc

    def __le__(self, other) -> bool:
        """ Метод для оператора <= """
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")

        sc = other if isinstance(other, int) else other.salary['to']

        if self.salary['from'] and self.salary['to']:
            return self.salary['from'] <= sc and self.salary['to'] <= sc
        elif self.salary['from']:
            return self.salary['from'] <= sc
        elif self.salary['to']:
            return self.salary['to'] <= sc

    @staticmethod
    def validate_salaries(value: int) -> int:
        """ Метод для валидации зарплаты"""
        try:
            if value:
                return value
        except TypeError:
            return 0
        else:
            return 0

    def create_dict(self) -> dict:
        """ Метод для представления экземпляра класса в виде словаря """
        return {
            "id": self.id,
            "name": self.name,
            "URL": self.url,
            "published_at": self.published_at,
            "salary": {'from': self.salary['from'], 'to': self.salary['to'], 'currency': self.salary['currency']},
            "snippet": self.snippet
        }

    @classmethod
    def create_object(cls, *args, **kwargs):
        """ Метод для альтернативного способа создания объекта"""
        return cls(*args, **kwargs)

    @classmethod
    def cast_to_object_list(cls, list_vacancies_json: list) -> list:
        """ Метод для преобразования набора данных из JSON в список объектов"""
        list_vacancy = []
        for v in list_vacancies_json:
            vacancy = cls.create_object(
                v['id'], v['name'], v['alternate_url'], v['published_at'], v['salary'], v['snippet']['requirement']
            )
            list_vacancy.append(vacancy)
        return list_vacancy

    def get_str_salary(self):
        """ Метод возвращает строковое представление salary """
        if self.salary['from'] and self.salary['to']:
            if self.salary['from'] != self.salary['to']:
                return f"{self.salary['from']} - {self.salary['to']} {self.salary['currency']}"
            else:
                return f"{self.salary['from']} {self.salary['currency']}"
        elif self.salary['from']:
            return f"от {self.salary['from']} {self.salary['currency']}"
        elif self.salary['to']:
            return f"до {self.salary['to']} {self.salary['currency']}"
        return f"не задана"
