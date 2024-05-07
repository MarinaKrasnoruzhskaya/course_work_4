import json
import os

from config import ROOT_DIR
from src.file_saver import FileSaver


class JSONSaver(FileSaver):
    """
    Класс для работы с JSON-файлами
    """
    def __init__(self):
        self.path_file = os.path.join(ROOT_DIR, "data", "vacancies.json")

    def add_vacancy(self, data: list):
        """ Метод для добавления списка вакансий в файл"""
        try:
            data_file = self.get_vacancy()
            print(data_file)
            i = len(data_file)
            self.delete_vacancy()

            for item1 in data:
                if item1 not in data_file:
                    data_file.append(item1)

        except (FileNotFoundError, ValueError):
            data_file = data
            i = 0
        with open(self.path_file, 'w', encoding="utf-8") as json_file:
            json.dump(data_file, json_file, ensure_ascii=False, indent=4)

        print(f'{len(data_file) - i} вакансии успешно записаны в файл {self.path_file}')

    def get_vacancy(self):
        """Метод возвращает список вакансий из файла"""
        with open(self.path_file, encoding="utf-8") as json_file:
            return json.load(json_file)

    def delete_vacancy(self):
        """ Метод для удаления вакансий"""
        with open(self.path_file, "w") as f:
            pass
