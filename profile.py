from filter import Filter
from specialization import Specialization
from list_of_specialization import List_of_specialization


def is_float(element: any) -> bool:
    # Проверка, того что элемент это число с плавающей запятой
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def is_int(element: any) -> bool:
    # Проверка, того что элемент это целое число
    if element is None:
        return False
    try:
        int(element)
        return True
    except ValueError:
        return False


class Profile:
    # Это класс в котором будет храниться информация о профиле вакансии
    # или человека ищущего работу
    def __init__(self, name: str, placer: str, spec: list[Specialization], salary: float, place_work: list,
                 name_education: str, level_education: int, unique_skills: list[str], id: int, stars=None):
        # Это конструктор для класса Profile. name- ФИО, placer - соискатель объявления(компания или человек)
        # spec - специализация это будет лист в виде профессии и ее сужения
        # salary - зарплата, place_work - место где может работать(листом т.к. можно работать в разных городах)
        # work_exp_min, work_exp_max - минимальный и максимальный уровень работы,
        # name_education, level_education - название и степень полученная образования
        # unique_skills- уникальные умения (водительские права, права на ношение оружия и тд)
        # id - уникальный номер для профиля, stars - оценки

        self.name = name
        self.placer = placer
        self.spec = spec
        self.salary = salary
        self.place_work = place_work
        self.name_education = name_education
        # Какие ступени образования могут быть?
        self.level_education = level_education
        self.unique_skills = unique_skills
        self.id = id
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

    def read_from_console(self, list_of_spec: List_of_specialization):
        # Функция читает из консоли информацию для анкеты,
        # Функция сделана с проверками для дурака, но не факт что со всеми возможными
        self.name = input('Ведите ФИО или название вашей Организации\n')
        placer = input('Ведите "соискатель" или "организация"\n')
        while placer != 'соискатель' and placer != 'организация':
            placer = input('Ведите "соискатель" или "организация"\n')
            print(placer != 'соискатель', placer != 'организация')
        if placer == "организация":
            self.placer = 1
        else:
            self.placer = 0

        buff = input('Ведите количество специализаций\n')
        while not is_int(buff):
            buff = input('Количество специализаций должно быть целым\n')
        buff = int(buff)
        if self.placer == 1:
            for i in range(buff):
                spec_name = list(input('Введите название специализации через запятую(", ")\n').split(', '))
                min_exp = input('Ведите минимальный стаж работы(если эта информация не важна, то введите 0)\n')
                while not is_float(min_exp):
                    min_exp = input('Минимальный стаж работы - это вещественное число\n')
                min_exp = float(min_exp)
                max_exp = input('Ведите максимальный стаж работы(если эта информация не важна, то введите 100)\n')
                while not is_float(max_exp) or float(max_exp) < min_exp:
                    max_exp = input('Максимальный стаж работы - это вещественное число не меньшее минимального стажа\n')
                max_exp = float(max_exp)
                new_spec = Specialization(spec_name, min_exp, max_exp)
                while new_spec not in list_of_spec.specializations:
                    print('Специализации нет в базе данных, попробуйте ввести ее по другому')
                    new_spec.profession = list(
                        input('Введите название специализации через запятую(", ")\n').split(', '))
        else:
            for i in range(buff):
                spec_name = list(input('Введите название специализации через запятую(", ")\n').split(', '))
                min_exp = input('Ведите стаж работы\n')
                while not is_float(min_exp):
                    min_exp = input('Стаж работы - это вещественное число\n')
                min_exp = float(min_exp)
                new_spec = Specialization(spec_name, min_exp, min_exp)
                while new_spec not in list_of_spec.specializations:
                    print('Специализации нет в базе данных, попробуйте ввести ее по другому')
                    new_spec.profession = list(
                        input('Введите название специализации через запятую (", ")\n').split(', '))
        self.salary = input('Ведите зарплату\n')
        while not is_float(buff):
            self.salary = input('Зарплата должна быть вещественной\n')
        self.salary = int(self.salary)
        self.place_work = list(input('Введите через запятую места работы\n').split(', '))
        if self.placer == 0:
            self.name_education = input('Введите ваше образование\n')
        # !! Здесь нужно будет выводить степени образования чтобы пользователь сам их определил
        self.level_education = input('Ведите степень образования\n')
        while not is_int(self.level_education):
            self.level_education = input('Степень образования быть целой\n')
        self.level_education = int(self.level_education)
        self.unique_skills = list(input('Введите через запятую уникальные умения или возможности\n' +
                                        'Например: Водительские права категории\n' +
                                        'Если нет таковых оставьте это поле пустым').split(', '))

