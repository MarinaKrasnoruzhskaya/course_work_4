import pytest

from src.exceptions import EmptyList
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies, \
    get_end_word_vacancy


def test_filter_vacancies(list_vacancies_test):
    filter_list_vacancies_test = filter_vacancies(list_vacancies_test, ['python'])
    assert len(filter_list_vacancies_test) == 2


def test_filter_vacancies_error(list_vacancies_test):
    with pytest.raises(EmptyList):
        filter_vacancies(list_vacancies_test, ['java'])


def test_get_vacancies_by_salary(list_vacancies_test_all):
    vacancies_by_salary_test = get_vacancies_by_salary(list_vacancies_test_all, '70000 - 180000')
    assert len(vacancies_by_salary_test) == 3


def test_get_vacancies_by_salary_error_empty_list(list_vacancies_test):
    with pytest.raises(EmptyList):
        get_vacancies_by_salary(list_vacancies_test, '80000 - 200000')


def test_get_vacancies_by_salary_error_input(list_vacancies_test):
    with pytest.raises(EmptyList):
        get_vacancies_by_salary(list_vacancies_test, '')


def test_get_vacancies_by_salary_error_input_2(list_vacancies_test):
    with pytest.raises(EmptyList):
        get_vacancies_by_salary(list_vacancies_test, '20000 - 2OOOOO')


def test_sort_vacancies(list_vacancies_test_2):
    sort_vacancies_test = sort_vacancies(list_vacancies_test_2)
    assert sort_vacancies_test[0].id == '98589456'

    sort_vacancies_test = sort_vacancies([])
    assert len(sort_vacancies_test) == 0


def test_get_top_vacancies(list_vacancies_test_all):
    top_vacancies_test = get_top_vacancies(list_vacancies_test_all, 2)
    assert len(top_vacancies_test) == 2


def test_print_vacancies(capsys, list_vacancies_test):
    print_vacancies(list_vacancies_test)
    message = capsys.readouterr()
    assert message.out.strip() == (f'№ 1\n'
                                   f'ID: 96712260\n'
                                   f'Наименование: Python developer junior+\n'
                                   f'URL: https://hh.ru/vacancy/96712260\n'
                                   f'Опубликовано: 08.05.2024\n'
                                   f'Зарплата: 70000 - 100000 RUR\n'
                                   f'Требования: Опыт работы c ОС Linux. Знание Python 3.6+, веб-фреймоворков...\n'
                                   f'\n'
                                   f'№ 2\n'
                                   f'ID: 97613568\n'
                                   f'Наименование: Python Developer\n'
                                   f'URL: https://hh.ru/vacancy/97613568\n'
                                   f'Опубликовано: 22.04.2024\n'
                                   f'Зарплата: не задана\n'
                                   f'Требования: Опыт коммерческой разработки на Python от 2 лет(middle), от 4 '
                                   f'лет(senior). Владение ...')


def test_get_end_word_vacancy():
    assert get_end_word_vacancy(11) == 'й'
    assert get_end_word_vacancy(5) == 'й'
