import os

import pytest

from config import ROOT_DIR
from src.json_saver import JSONSaver


def test_json_saver_init(json_file_test):
    assert json_file_test.path_file == os.path.join(ROOT_DIR, "data", "test.json")


def test_json_saver_ad_vacancy(capsys,json_file_test, list_vacancies_from_dict_test, list_vacancies_from_dict_test_2):
    json_file_test.delete_vacancy()
    json_file_test.add_vacancy(list_vacancies_from_dict_test)
    message = capsys.readouterr()
    assert message.out.strip() == f"2 вакансии успешно записаны(а) в файл {json_file_test.path_file}"

    json_file_test.add_vacancy(list_vacancies_from_dict_test)
    message = capsys.readouterr()
    assert message.out.strip() == f"Все вакансии ранее уже были добавлены в файл"

    json_file_test.add_vacancy(list_vacancies_from_dict_test_2)
    message = capsys.readouterr()
    assert message.out.strip() == f"1 вакансия успешно записаны(а) в файл {json_file_test.path_file}"
