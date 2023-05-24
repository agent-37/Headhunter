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
    def __init__(self):
        # Это конструктор для класса Profile. name- ФИО, placer - соискатель объявления(компания или человек)
        # spec - специализация это будет лист в виде профессии и ее сужения
        # salary - зарплата, place_work - место где может работать(листом т.к. можно работать в разных городах)
        # work_exp_min, work_exp_max - минимальный и максимальный уровень работы,
        # name_education, level_education - название и степень полученная образования
        # unique_skills- уникальные умения (водительские права, права на ношение оружия и тд)
        # id - уникальный номер для профиля, stars - оценки
        # ИЗНАЧАЛЬНО ДАННЫЕ МУСОРНЫЕ
        self.name = ''
        self.placer = 0
        self.spec = None
        self.salary = 0
        self.place_work = ''
        self.name_education = ''
        self.level_education = 0
        self.unique_skills = []
        self.id = 0
        self.stars = [0, 0, 0, 0, 0]
        self.feedback_added = 0

    def setter(self, name: str, placer: int, spec: list[Specialization], salary: float, place_work: list,
                 name_education: str, level_education: int, unique_skills: list[str], id: int, stars=None):
        # Это сеттер
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

    def print_all_info(self):
        # Функция для вывода всей информации о профиле в консоль
        if self.placer == 0:
            print('Имя пользователя:', self.name)
            print('Соискатель')
        else:
            print('Название организации:', self.name)
            print('Работодатель')
        print('Предлагаемая работа:')
        for vocation in self.spec:
            vocation.print_specialization()
            if self.placer == 0:
                print('Стаж:', vocation.work_exp_max, 'лет')
            else:
                if vocation.work_exp_min == 0 and vocation.work_exp_max == 100:
                    print('Стаж: не важен')
                elif vocation.work_exp_min == 0:
                    print('Стаж: до', vocation.work_exp_max, 'лет')
                elif vocation.work_exp_max == 100:
                    print('Стаж: от', vocation.work_exp_min, 'лет')
                else:
                    print('Стаж: от', vocation.work_exp_min, 'до', vocation.work_exp_max, 'лет')
        print('Предлагаемая заработная плата:', self.salary)
        print('Города:', end=' ')
        for idx in range(len(self.place_work)-1):
            print(self.place_work[idx], end=', ')
        print(self.place_work[-1])
        if self.placer == 0:
            print('Законченное учебное заведение:', self.name_education)
        print('Уровень образования:', end=' ')
        match self.level_education:
            case(0): print('отсутствует')
            case(1): print('основное общее (9 классов)')
            case(2): print('среднее общее (11 классов)')
            case(3): print('среднее профессиональное')
            case(4): print('высшее I степени (бакалавриат)')
            case(5): print('высшее II степени (специалитет, магистратура)')
            case(6): print('высшее III степени (подготовка кадров высшей квалификации)')
        if len(self.unique_skills) != 0:
            print('Особые умения:')
            for skill in self.unique_skills:
                print(skill)
        if self.placer == 0:
            print('Оценки аккаунта:')
            for idx in range(6):
                print(idx,':', '*' * self.stars.count(idx))

    def print_some_info(self):
        # Функция для вывода частичной информации о профиле в консоль
        if self.placer == 0:
            print('Имя пользователя:', self.name)
            print('Соискатель')
        else:
            print('Название организации:', self.name)
            print('Работодатель')
        print('Предлагаемая работа:')
        for vocation in self.spec:
            vocation.print_specialization()
        print('Предлагаемая заработная плата:', self.salary)
        print('Города:', end=' ')
        for idx in range(len(self.place_work) - 1):
            print(self.place_work[idx], end=', ')
        print(self.place_work[-1])

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
        if filter.unique_skills is not None:
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
                if one_spec.is_nested(filter.spec):
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

    def change_profile(self):
        # функция на данный момент максимально сырая и по большей части заглушка
        print('Параметры, доступные для изменения:\n'
              '1. Имя пользователя/организации\n'
              '2. Роль соискателя объявления\n'
              '3. Профессия\n'
              '4. Стаж работы\n'
              '5. Заработная плата\n'
              '6. Место работы\n'
              '7. Место и уровень образования\n'
              '8. Особые умения')
        item_number = int(input('Выберите параметр, который хотите изменить: '))
        match item_number:
            case 1:
                new_name = input('Введите новое имя пользователя/организации: ')
                flag = False
                while new_name == self.name and flag == False:
                    print('Новое имя совпадает с предыдущим. Хотите изменить его?\n'
                          '1. Да, ввести имя еще раз\n'
                          '2. Нет, сохранить текущее имя')
                    number = int(input('Выберите пункт: '))
                    match number:
                        case 1:
                            new_name = input('Введите новое имя пользователя/организации: ')
                        case 2:
                            flag = True
                self.name = new_name
            case 2:
                print('Ваша текущая роль -', end = ' ')
                if self.placer == 0:
                    print('\'соискатель\'', end = '. ')
                else:
                    print('\'работодатель\'', end = '. ')
                print('Хотите поменять роль?\n'
                      '1. Да\n'
                      '2. Нет')
                number = int(input('Выберите пункт: '))
                if number == 1:
                    self.placer = abs(self.placer - 1)
            case 3:
                # добавление/удаление 1 профессии (может нескольких) и проверка на корректность
                print('Доступные действия:\n'
                      '1. Добавить професию\n'
                      '2. Удалить профессию')
            case 4:
                print('Список ваших профессий:')
                idx = 1
                for vocation in self.spec:
                    print(idx, end = ': ')
                    vocation.print_specialization()
                    idx = idx + 1
                # тут закончила
            case 5:
                new_salary = int(input('Введите новую заработную плату: '))  # сделать проверку на совпадение со старой зарплатой
                self.salary = new_salary
            case 6:
                # добавление/удаление 1 города (может нескольких) и проверка на корректность
                print('Доступные действия:\n'
                      '1. Добавить город\n'
                      '2. Удалить город')
            case 7:
                # нужна проверка на корректность
                print('Доступные действия:\n'
                      '1. Изменить последнее место обучения\n'
                      '2. Изменить уровень обучения')
                number = int(input('Выберите пункт: '))
                if number == 1:
                    new_name = input('Введите новое образовательное учреждение: ')
                    self.name_education = new_name
                else:
                    new_level = int(input('Введите новый уровень образования: '))
                    self.level_education = new_level
            case 8:
                # добавление/удаление 1 особого умения (может нескольких) и проверка на корректность
                print('Доступные действия:\n'
                      '1. Добавить особое умение\n'
                      '2. Удалить особое умение')
                number = int(input('Выберите пункт: '))