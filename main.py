from src.exceptions import EmptyList
from src.hh import HH
from src.json_saver import JSONSaver
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies, \
    get_vacancies_list_from_dict
from src.vacancy import Vacancy


def user_interaction():
    """ Функция для взаимодействия с пользователем """
    hh_api = HH()

    search_vacancies = input("Введите название вакансии: ")

    try:
        hh_vacancies = hh_api.get_vacancies(search_vacancies)
        vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

        answer = ''
        while answer not in ('stop', 'стоп'):
            filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
            try:
                filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

                while answer not in ('stop', 'стоп'):
                    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

                    try:
                        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

                        sorted_vacancies = sort_vacancies(ranged_vacancies)

                        while answer not in ('stop', 'стоп'):
                            try:
                                top_n = int(input("Введите количество вакансий для вывода в топ N: "))

                                if top_n > len(sorted_vacancies):
                                    print(f'\nК сожалению, было найдено всего {len(sorted_vacancies)} вакансий')

                                top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

                                print_vacancies(top_vacancies)

                                user_selection = input(
                                    "Напишите all - для создания файла c выбранными вакансиями, напишите new - для "
                                    "добавления в файл новых вакансий или напишите stop - если не хочешь вакансии \n"
                                    "записывать в файл: "
                                ).lower().strip()

                                if user_selection not in ('stop', 'стоп'):
                                    json_saver = JSONSaver()

                                    if user_selection == 'all':
                                        json_saver.delete_vacancy()

                                    json_saver.add_vacancy(get_vacancies_list_from_dict(top_vacancies))

                                answer = 'stop'
                            except ValueError:
                                print("Неправильный ввод значений: количество вакансий должно быть целым числом")
                                answer = input(
                                    "Напишите stop - для завершения поиска или нажмите Enter - для ввода другого "
                                    "количества вакансий: "
                                ).lower().strip()

                    except EmptyList as e:
                        print(e)
                        answer = input(
                            "Напишите stop - для завершения поиска или нажмите Enter - для ввода другого диапазона "
                            "зарплат: "
                        ).lower().strip()
            except EmptyList as e:
                print(e)
                answer = input(
                    'Напишите stop - для завершения поиска или нажмите Enter - для ввода других ключевых слов: '
                ).lower().strip()
    except EmptyList as e:
        print(e)


if __name__ == "__main__":
    user_interaction()
