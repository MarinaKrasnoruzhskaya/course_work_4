import pytest

from src.exceptions import EmptyList


def test_hh_init(hh_api_test):
    assert hh_api_test.url == 'https://api.hh.ru/vacancies'
    assert hh_api_test.headers == {'User-Agent': 'HH-User-Agent'}
    assert hh_api_test.params == {'text': '', 'page': 0, 'per_page': 100, 'area': 113}
    assert hh_api_test.vacancies == []


def test_hh_get_vacancies(hh_api_test):
    hh_api_test.get_vacancies('python-developer')
    assert len(hh_api_test.vacancies) > 0


def test_hh_get_vacancies_error(hh_api_test):
    with pytest.raises(EmptyList):
        hh_api_test.get_vacancies('jhghfhg')
