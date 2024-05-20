import csv

from src.file_saver import FileSaver


class CSVSaver(FileSaver):
    """
    Класс для работы с csv-файлами
    """
    def __init__(self, name="vacancies.csv"):
        super().__init__(name)

    def __str__(self):
        pass

    def add_vacancy(self, data: list):
        keys = ['id', 'name', 'URL', 'published_at', 'salary from', 'salary to', 'snippet']
        with open(self.path_file, 'w', encoding='cp1251', newline='') as file:
            writer = csv.writer(file, delimiter=';', lineterminator='\r')
            writer.writerow(keys)
            for v in data:
                writer.writerow([v.id, v.name, v.url, v.published_at, v.salary['from'], v.salary['to'], v.snippet])

    def get_vacancy(self):
        with open(self.path_file, 'w', encoding='cp1251', newline='') as file:
            file_reader = csv.reader(file, delimiter=';')
        print(file_reader)
        return file_reader

    def delete_vacancy(self):
        pass


csv_saver = CSVSaver()
csv_saver.get_vacancy()
