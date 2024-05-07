from src.exceptions import EmptyList


def filter_vacancies(list_vacancies: list, word_filter: list) -> list:
    """ Функция возвращает отфильтрованный список вакансий по ключевым словам"""
    list_filter_vacancies = [
        vac for vac in filter(
            lambda v:
            set(word_filter) <= set(f"{f'{v.id}'.lower()} "
                                    f"{v.name.lower()} "
                                    f"{v.url.lower()} "
                                    f"{v.published_at.lower()} "
                                    f"{f'{v.salary['from']}'.lower()} "
                                    f"{f'{v.salary['to']}'.lower()} "
                                    f"{v.salary['currency'].lower()} "
                                    f"{v.snippet.lower()}".split()),
            list_vacancies
        )
    ]

    if not list_filter_vacancies:
        raise EmptyList('Ключевые слова не найдены в списке вакансий')
    return list_filter_vacancies


def get_vacancies_by_salary(vacancies: list, range_salary: str) -> list | None:
    """ Функция возвращает список вакансий в заданном диапазоне зарплат"""
    try:
        s_min, s_max = range_salary.split('-')
        s_min, s_max = int(s_min.strip()), int(s_max.strip())
        vacancy_by_salary = [v for v in vacancies if (s_min <= v <= s_max)]

        if not vacancy_by_salary:
            raise EmptyList('В заданном диапазоне вакансии не найдены')
        return vacancy_by_salary

    except ValueError:
        print('Диапазон зарплат не задан или задан не верно')
        raise EmptyList('Необходимо указать другой диапазон зарплат')


def sort_vacancies(vacancies_for_sorting: list) -> list:
    """ Функция возвращает отсортированный по убыванию список вакансий по дате опубликования"""
    if vacancies_for_sorting:
        return sorted(vacancies_for_sorting, key=lambda v: v.published_at, reverse=True)
    return []


def get_top_vacancies(vac_list: list, top: int) -> list:
    """ Функция возвращает top вакансий"""
    return vac_list[:top]


def print_vacancies(vacancies: list) -> None:
    """ Функция выводит на печать список вакансий"""
    i = 0
    for vacancy in vacancies:
        i += 1
        print(f"№ {i}\n{str(vacancy)}")


def get_vacancies_list_from_dict(vacancies_list: list) -> list:
    """ Функция возвращает список вакансий, преобразованных в словарь"""
    return [v.create_dict() for v in vacancies_list]
