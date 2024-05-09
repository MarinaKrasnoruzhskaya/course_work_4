import pytest

from src.hh import HH
from src.json_saver import JSONSaver
from src.utils import get_vacancies_list_from_dict
from src.vacancy import Vacancy


@pytest.fixture
def first_vacancy():
    return Vacancy(
        "96712260",
        "Python developer junior+",
        "https://hh.ru/vacancy/96712260",
        "2024-05-08T12:54:04+0300",
        {
            "from": 70000,
            "to": 100000,
            "currency": "RUR"
        },
        "Опыт работы c ОС Linux. Знание Python 3.6+, веб-фреймоворков..."
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        "97613568",
        "Python Developer",
        "https://hh.ru/vacancy/97613568",
        "2024-04-22T12:54:04+0300",
        None,
        "Опыт коммерческой разработки на Python от 2 лет(middle), от 4 лет(senior). Владение ..."
    )


@pytest.fixture
def third_vacancy():
    return Vacancy(
        "97406236",
        "Разработчик Backend",
        "https://hh.ru/vacancy/97406236",
        "2024-05-06T12:54:04+0300",
        {
            "from": 180000,
            "to": 0,
            "currency": "RUR"
        },
        "умение применять на практике шаблоны проектирования. - опыт разработки на Python 3..."
    )


@pytest.fixture
def fourth_vacancy():
    return Vacancy(
        "98589456",
        "Lead Python Developer",
        "https://hh.ru/vacancy/98589456",
        "2024-05-08T12:54:04+0300",
        {
            "from": 0,
            "to": 400000,
            "currency": "RUR"
        },
        "СТРОГО уверенное знание python3 и нескольких других языков..."
    )


@pytest.fixture
def fifth_vacancy():
    return Vacancy(
        "98477026",
        "Сетевой инженер",
        "https://hh.ru/vacancy/98477026",
        "2024-05-06T12:54:04+0300",
        {
            "from": 175000,
            "to": 175000,
            "currency": "RUR"
        },
        "Будет плюсом: - Опыт работы с системами мониторинга Zabbix, Grafana. - Знание Python в части ..."
    )


@pytest.fixture
def json_data():
    return [
        {'id': '98565084', 'premium': False, 'name': 'Frontend Javascript разработчик', 'department': None,
         'has_test': True, 'response_letter_required': False,
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': {'from': 120000, 'to': 180000, 'currency': 'RUR', 'gross': False},
         'type': {'id': 'open', 'name': 'Открытая'},
         'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-05-07T17:36:42+0300', 'created_at': '2024-05-07T17:36:42+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=98565084',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/98565084?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/98565084',
         'snippet': {
             'requirement': 'Вы не только умеете писать работающий код на JS, но и знаете как он работает '
                            '(Vanilla.JS, ES5, ES6...',
             'responsibility': 'Разработка комплексных SPA-приложений, взаимодействие с различными API и внутренними '
                               'сервисами. Написание производительного и отказоустойчивого кода на JavaScript используя '
                               'современные...'}},
        {'id': '98634244', 'premium': False, 'name': 'Python Junior разработчик', 'department': None, 'has_test': False,
         'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': None, 'type': {'id': 'open', 'name': 'Открытая'},
         'sort_point_distance': None, 'published_at': '2024-05-08T18:47:54+0300',
         'created_at': '2024-05-08T18:47:54+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=98634244',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/98634244?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/98634244',
         'relations': [],
         'snippet': {
            'requirement': 'Опыт работы с Python от 1.5 года. Опыт работы с Flack. Знание Docker на уровне пользователя. '
                           'Знание Linux на...',
            'responsibility': 'Систематизировать, переписывать конфликтующие микросервисы. Исправлять ошибки в коде, '
                              'найденные тестировщиком. Участвовать в планировании и постановке задач.'}}
    ]


@pytest.fixture
def json_file_test():
    return JSONSaver("test.json")


@pytest.fixture
def list_vacancies_from_dict_test(first_vacancy, second_vacancy):
    return get_vacancies_list_from_dict([first_vacancy, second_vacancy])


@pytest.fixture
def list_vacancies_from_dict_test_2(first_vacancy, third_vacancy):
    return get_vacancies_list_from_dict([first_vacancy, third_vacancy])


@pytest.fixture
def hh_api_test():
    return HH()


@pytest.fixture
def list_vacancies_test(first_vacancy, second_vacancy):
    return [first_vacancy, second_vacancy]


@pytest.fixture
def list_vacancies_test_all(first_vacancy, second_vacancy, third_vacancy, fourth_vacancy, fifth_vacancy):
    return [first_vacancy, second_vacancy, third_vacancy, fourth_vacancy, fifth_vacancy]


@pytest.fixture
def list_vacancies_test_2(second_vacancy, third_vacancy, fourth_vacancy):
    return [second_vacancy, third_vacancy, fourth_vacancy]
