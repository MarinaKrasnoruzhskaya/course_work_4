import json

from src.file_saver import FileSaver
from src.utils import get_end_word_vacancy


class JSONSaver(FileSaver):
    """
    Класс для работы с JSON-файлами
    """
    def __init__(self, name="vacancies.json"):
        super().__init__(name)

    def add_vacancy(self, data: list):
        """ Метод для добавления списка вакансий в файл"""
        try:
            data_file = self.get_vacancy()
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

        count = len(data_file) - i
        if count:
            print(f'{count} ваканси{get_end_word_vacancy(count)} успешно записаны(а) в файл {self.path_file}')
        else:
            print('Все вакансии ранее уже были добавлены в файл')

    def get_vacancy(self):
        """Метод возвращает список вакансий из файла"""
        with open(self.path_file, encoding="utf-8") as json_file:
            return json.load(json_file)

    def delete_vacancy(self):
        """ Метод для удаления вакансий"""
        with open(self.path_file, "w") as f:
            pass
