import pytest

from src.vacancy import Vacancy


def test_vacancy_init(first_vacancy):
    assert first_vacancy.id == "96712260"
    assert first_vacancy.name == "Python developer junior+"
    assert first_vacancy.url == "https://hh.ru/vacancy/96712260"
    assert first_vacancy.published_at == "2024-05-08T12:54:04+0300"
    assert first_vacancy.salary == {"from": 70000, "to": 100000, "currency": "RUR"}
    assert first_vacancy.snippet == "Опыт работы c ОС Linux. Знание Python 3.6+, веб-фреймоворков..."


def test_vacancy_init_salary_none(second_vacancy):
    assert second_vacancy.salary == {'from': 0, 'to': 0, 'currency': ''}


def test_vacancy_str(first_vacancy):
    assert str(first_vacancy) == (f'ID: 96712260\n'
                                  f'Наименование: Python developer junior+\n'
                                  f'URL: https://hh.ru/vacancy/96712260\n'
                                  f'Опубликовано: 08.05.2024\n'
                                  f'Зарплата: 70000 - 100000 RUR\n'
                                  f'Требования: Опыт работы c ОС Linux. Знание Python 3.6+, '
                                  f'веб-фреймоворков...\n')


def test_vacancy_ge(first_vacancy, second_vacancy, third_vacancy, fourth_vacancy):
    assert (first_vacancy >= 50000) == True
    assert (first_vacancy >= second_vacancy) == True
    assert (third_vacancy >= first_vacancy) == True
    assert (fourth_vacancy >= first_vacancy) == True


def test_vacancy_ge_type_error(first_vacancy):
    with pytest.raises(TypeError):
        assert first_vacancy >= '20000'


def test_vacancy_le(first_vacancy, second_vacancy, third_vacancy, fourth_vacancy):
    assert (first_vacancy <= 500000) == True
    assert (first_vacancy <= second_vacancy) == False
    assert (third_vacancy <= first_vacancy) == False
    assert (fourth_vacancy <= first_vacancy) == False


def test_vacancy_le_type_error(first_vacancy):
    with pytest.raises(TypeError):
        assert first_vacancy <= '20000'


def test_vacancy_validate_salaries():
    v = Vacancy(
            "Test",
            "Test",
            "Test",
            "2024-05-08T12:54:04+0300",
            {"from": '123', "to": 400000, "currency": "RUR"},
            "Test"
        )
    assert v.salary['from'] == 0


def test_vacancy_create_dict(first_vacancy):
    assert first_vacancy.create_dict() == {
        "id": "96712260",
        "name": "Python developer junior+",
        "URL": "https://hh.ru/vacancy/96712260",
        "published_at": "2024-05-08T12:54:04+0300",
        "salary": {'from': 70000, 'to': 100000, 'currency': "RUR"},
        "snippet": "Опыт работы c ОС Linux. Знание Python 3.6+, веб-фреймоворков..."
    }


def test_vacancy_create_object(first_vacancy):
    v = Vacancy.create_object("96712260", "Python developer junior+", "https://hh.ru/vacancy/96712260",
                                 "2024-05-08T12:54:04+0300", {"from": 70000, "to": 100000, "currency": "RUR"},
                                 "Опыт работы c ОС Linux. Знание Python 3.6+, веб-фреймоворков...")
    assert v.id == "96712260"
    assert v.name == "Python developer junior+"
    assert v.url == "https://hh.ru/vacancy/96712260"
    assert v.published_at == "2024-05-08T12:54:04+0300"
    assert v.salary == {"from": 70000, "to": 100000, "currency": "RUR"}
    assert v.snippet == "Опыт работы c ОС Linux. Знание Python 3.6+, веб-фреймоворков..."


def test_vacancy_cast_to_object_list(json_data):
    v_list = Vacancy.cast_to_object_list(json_data)
    assert len(v_list) == 2


def test_vacancy_get_str_salary(first_vacancy, second_vacancy, third_vacancy, fourth_vacancy, fifth_vacancy):
    assert first_vacancy.get_str_salary() == "70000 - 100000 RUR"
    assert second_vacancy.get_str_salary() == "не задана"
    assert third_vacancy.get_str_salary() == "от 180000 RUR"
    assert fourth_vacancy.get_str_salary() == "до 400000 RUR"
    assert fifth_vacancy.get_str_salary() == "175000 RUR"
