from filter import Filter
from specialization import Specialization
from list_of_specialization import List_of_specialization


class Profile:
    # Это класс в котором будет храниться информация о профиле вакансии
    # или человека ищущего работу
    def __init__(self, name: str, placer: str, spec: list[Specialization], salary: float, place_work: list,
                 name_education: str, level_education: int, unique_skills: list[str], stars=None):
        # Это конструктор для класса Profile. name- ФИО, placer - соискатель объявления(компания или человек)
        # spec - специализация это будет лист в виде профессии и ее сужения
        # salary - зарплата, place_work - место где может работать(листом т.к. можно работать в разных городах)
        # work_exp_min, work_exp_max - минимальный и максимальный уровень работы,
        # name_education, level_education - название и степень полученная образования
        # unique_skills- уникальные умения (водительские права, права на ношение оружия и тд)
        # stars - оценки

        self.name = name
        self.placer = placer
        self.spec = spec
        self.salary = salary
        self.place_work = place_work
        self.name_education = name_education
        # Какие ступени образования могут быть?
        self.level_education = level_education
        self.unique_skills = unique_skills
        self.stars = stars

    def print_info(self):
        # Функция для вывода информации о профиле в консоль
        # Пока здесь будет заглушка !!!!! потом сделаем нормальную реализацию
        print(self.name)

    def test_worthiness(self, filter: Filter) -> bool:
        # проверка на то, что профиль подходит под условия заданные пользователем(filter)
        if filter.check_correct() is not True:
            return False
        if filter.name is not None and filter.name != self.name \
                or filter.placer is not None and filter.placer != self.placer \
                or filter.min_salary is not None and filter.min_salary > self.salary \
                or filter.max_salary is not None and filter.max_salary < self.salary \
                or filter.place_work is not None and filter.place_work not in self.place_work \
                or filter.level_education is not None and filter.level_education > self.level_education:
            return False

        count_unique_skills = 0
        for skill in self.unique_skills:
            for need_skill in filter.unique_skills:
                if need_skill == skill:
                    count_unique_skills += 1
                    break

        if count_unique_skills != len(filter.unique_skills):
            return False

        if filter.spec is not None:
            for one_spec in self.spec:
                if filter.spec.is_nested(one_spec):
                    return True

        return False

    def check_all_spec_correct(self, list_of_spec: List_of_specialization) -> bool:
        if len(self.spec) == 0:
            return False
        for spec in self.spec:
            if spec not in list_of_spec.specializations:
                return False

        return True
