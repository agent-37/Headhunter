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
        self.spec = []
        self.salary = 0
        self.place_work = []
        self.name_education = ''
        self.level_education = 0
        self.unique_skills = []
        self.id = 0
        self.stars = []
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
                while not is_float(min_exp) or float(min_exp) < 0:
                    min_exp = input('Минимальный стаж работы - это вещественное число\n')
                min_exp = float(min_exp)
                max_exp = input('Ведите максимальный стаж работы(если эта информация не важна, то введите 100)\n')
                while not is_float(max_exp) or float(max_exp) < min_exp or float(max_exp) < 0:
                    max_exp = input('Максимальный стаж работы - это вещественное число не меньшее минимального стажа\n')
                max_exp = float(max_exp)
                new_spec = Specialization(spec_name, min_exp, max_exp)
                while new_spec not in list_of_spec.specializations:
                    print('Специализации нет в базе данных, попробуйте ввести ее по другому')
                    new_spec.profession = list(
                        input('Введите название специализации через запятую(", ")\n').split(', '))
                self.spec.append(new_spec)
        else:
            for i in range(buff):
                spec_name = list(input('Введите название специализации через запятую(", ")\n').split(', '))
                min_exp = input('Ведите стаж работы\n')
                while not is_float(min_exp) or float(min_exp):
                    min_exp = input('Стаж работы - это вещественное число\n')
                min_exp = float(min_exp)
                new_spec = Specialization(spec_name, min_exp, min_exp)
                while new_spec not in list_of_spec.specializations:
                    print('Специализации нет в базе данных, попробуйте ввести ее по другому')
                    new_spec.profession = list(
                        input('Введите название специализации через запятую (", ")\n').split(', '))
                self.spec.append(new_spec)
        buff = input('Ведите зарплату\n')
        while not is_float(buff):
            buff = input('Зарплата должна быть вещественной\n')
        self.salary = int(buff)
        self.place_work = list(input('Введите через запятую места работы\n').split(', '))
        if self.placer == 0:
            self.name_education = input('Введите ваше образование\n')
        # !! Здесь нужно будет выводить степени образования чтобы пользователь сам их определил
        buff = input('Ведите степень образования\n')
        while not is_int(buff) or int(buff) < 0 or int(buff) > 6:
            buff = input('Степень образования быть целой\n')
        self.level_education = int(buff)
        self.unique_skills = list(input('Введите через запятую уникальные умения или возможности\n' +
                                        'Например: Водительские права категории\n' +
                                        'Если нет таковых оставьте это поле пустым').split(', '))

    def change_profile(self, list_ : List_of_specialization):
        # функция изменения профиля пользователем с консоли
        print('Параметры, доступные для изменения:', '1. Имя пользователя/организации', '2. Профессия и стаж работы',
              '3. Заработная плата', '4. Место работы', '5. Место и уровень образования',
              '6. Особые умения', '7. Выход', sep='\n')
        while True:
            item_number = input('Выберите параметр, который хотите изменить: ')
            match item_number:
                case '1':
                    print('Текущее имя пользователя:', self.name)
                    new_name = input('Введите новое имя пользователя/организации: ')
                    self.name = new_name
                case '2': self.change_profile_spec_by_console(list_)
                case '3': self.change_profile_salary_by_console()
                case '4': self.change_profile_town_by_console()
                case '5': self.change_profile_education_by_console()
                case '6': self.change_profile_unique_skills_by_console()
                case '7': return
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_profile_salary_by_console(self):
        # функция изменения зарплаты пользователя через консоль
        print('Текующая заработная плата:', self.salary)
        new_salary = input('Введите новую заработную плату: ')
        while not is_float(new_salary) or float(new_salary) < 0:
            new_salary = input('Некорректные данные. Повторите ввод: ')
        self.salary = float(new_salary)

    def change_profile_education_by_console(self):
        # функция изменения образования пользователя через консоль
        if self.placer == 0:
            print('Текущее образование:', self.name_education)
        print('Текущий уровень образования:', self.level_education)
        if self.placer == 0:
            print('Доступные действия:', '1. Изменить последнее место образования', '2. Изменить уровень образования', sep='\n')
            while True:
                number = input('Выберите пункт: ')
                match number:
                    case '1':
                        new_name_education = input('Введите новое образовательное учреждение: ')
                        self.name_education = new_name_education
                        return
                    case '2':
                        self.change_profile_level_education_by_console()
                        return
                    case _: print('Команда не была распознана. Попытайтесь еще раз')
        else:
            print('Хотите изменить уровень образования?', '1. Да', '2. Нет', sep='\n')
            while True:
                number = input('Выберите пункт: ')
                match number:
                    case '1':
                        self.change_profile_level_education_by_console()
                        return
                    case '2': return
                    case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_profile_level_education_by_console(self):
        # функция изменения уровня образования пользователя через консоль
        new_level = input('Введите новый уровень образования: ')
        while not is_int(new_level) or int(new_level) < 0 or int(new_level) > 6:
            new_level = input('Некорректные данные. Повторите ввод: ')
        self.level_education = int(new_level)

    def change_profile_town_by_console(self):
        # функция изменения города для работы пользователя через консоль
        print('Города:')
        for idx in range(len(self.place_work)):
            print(idx + 1, self.place_work[idx], sep=') ')
        print('Доступные действия:', '1. Добавить город', '2. Удалить город', sep='\n')
        while True:
            number = input('Выберите пункт: ')
            match number:
                case '1':
                    new_town = input('Введите новое место работы: ')
                    if new_town not in self.place_work:
                        self.place_work.append(new_town)
                    else:
                        print('Такой город уже находится в списке.')
                    return
                case '2':
                    if len(self.place_work) == 1:
                        print('Должен оставаться хотя бы 1 город.')
                        return
                    number = input('Выберите номер города, который хотите удалить: ')
                    while not is_int(number) or int(number) < 1 or int(number) > len(self.place_work):
                        number = input('Некорректные данные. Повторите ввод: ')
                    self.place_work.pop(int(number) - 1)
                    return
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_profile_unique_skills_by_console(self):
        # функция изменения особых умений пользователя через консоль
        if len(self.unique_skills) != 0:
            print('Особые умения:')
            for idx in range(len(self.unique_skills)):
                print(idx + 1, self.unique_skills[idx], sep=') ')
        else:
            print('Особые умения отсутствуют')
        print('Доступные действия:', '1. Добавить особое умение', '2. Удалить особое умение', sep='\n')
        while True:
            number = input('Выберите пункт: ')
            match number:
                case '1':
                    new_unique_skill = input('Введите новое особое умение: ')
                    if new_unique_skill not in self.unique_skills:
                        self.unique_skills.append(new_unique_skill)
                    else:
                        print('Такое умение уже находится в списке.')
                    return
                case '2':
                    if len(self.unique_skills) == 0:
                        print('Информация об уникальных умениях отсутствует.')
                        return
                    number = input('Выберите номер особого умения, который хотите удалить: ')
                    while not is_int(number) or int(number) < 1 or int(number) > len(self.unique_skills):
                        number = input('Некорректные данные. Повторите ввод: ')
                    self.unique_skills.pop(int(number) - 1)
                    return
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_profile_spec_by_console(self, list_ : List_of_specialization):
        # функция изменения специализации пользователя через консоль
        print('Текущая работа:')
        idx = 1
        for vocation in self.spec:
            print(idx, end=' ')
            vocation.print_specialization()
            idx = idx + 1
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
        print('Доступные действия:', '1. Добавить работу', '2. Удалить работу', '3. Изменить стаж у 1 работы', sep='\n')
        while True:
            number = input('Выберите пункт: ')
            match number:
                case '1':
                    temp_spec = Specialization([])
                    set_of_spec = list_.reduce_find_recommand(temp_spec)
                    while len(set_of_spec) != 0:
                        for spec in set_of_spec:
                            print(spec)
                        new_spec = input('Введите уточнение по работе: ')
                        while new_spec not in set_of_spec:
                            new_spec = input('Такая профессия некорректна. Выберите что-нибудь из предложенного списка: ')
                        temp_spec.profession.append(new_spec)
                        set_of_spec = list_.reduce_find_recommand(temp_spec)
                    if temp_spec in self.spec:
                        print('У вас уже имеется такая работа. Добавление не может быть произведено.')
                        return
                    if self.placer == 0:
                        work_exp = input('Введите стаж работы: ')
                        while not is_float(work_exp) or float(work_exp) < 0 or float(work_exp) > 100:
                            work_exp = input('Некорректные данные. Стаж работы должен выглядеть как число от 0 (если его нет) до 100 (если он не важен). Повторите ввод: ')
                        temp_spec.work_exp_min = float(work_exp)
                        temp_spec.work_exp_max = float(work_exp)
                    else:
                        work_exp = input('Введите минимальный стаж работы: ')
                        while not is_float(work_exp) or float(work_exp) < 0 or float(work_exp) > 100:
                            work_exp = input('Некорректные данные. Стаж работы должен выглядеть как число от 0 (если его нет) до 100 (если он не важен). Повторите ввод: ')
                        temp_spec.work_exp_min = float(work_exp)
                        work_exp = input('Введите максимальный стаж работы: ')
                        while not is_float(work_exp) or float(work_exp) < 0 or float(work_exp) > 100 or temp_spec.work_exp_min > float(work_exp):
                            work_exp = input('Некорректные данные. Стаж работы должен выглядеть как число от 0 (если его нет) до 100 (если он не важен). Повторите ввод: ')
                        temp_spec.work_exp_max = float(work_exp)
                    self.spec.append(temp_spec)
                    return
                case '2':
                    if len(self.spec) == 1:
                        print('Нужна хотя бы 1 работа.')
                        return
                    number = input('Выберите номер работы, который хотите удалить: ')
                    while not is_int(number) or int(number) < 1 or int(number) > len(self.spec):
                        number = input('Некорректные данные. Повторите ввод: ')
                    self.spec.pop(int(number) - 1)
                    return
                case '3':
                    number = input('Выберите номер работы, стаж который хотите изменить: ')
                    while not is_int(number) or int(number) < 1 or int(number) > len(self.spec):
                        number = input('Некорректные данные. Повторите ввод: ')
                    if self.placer == 0:
                        work_exp = input('Введите новый стаж работы: ')
                        while not is_float(work_exp) or float(work_exp) < 0 or float(work_exp) > 100:
                            work_exp = input('Некорректные данные. Стаж работы должен выглядеть как число от 0 (если его нет) до 100 (если он не важен). Повторите ввод: ')
                        self.spec[int(number) - 1].work_exp_min = float(work_exp)
                        self.spec[int(number) - 1].work_exp_max = float(work_exp)
                    else:
                        print('Доступные действия:', '1. Изменить минимальный стаж работы', '2. Изменить максимальный стаж работы', sep='\n')
                        while True:
                            number_ = input('Выберите пункт: ')
                            match number_:
                                case '1':
                                    work_exp = input('Введите новый стаж работы: ')
                                    while not is_float(work_exp) or float(work_exp) < 0 or float(work_exp) > 100:
                                        work_exp = input('Некорректные данные. Стаж работы должен выглядеть как число от 0 (если его нет) до 100 (если он не важен). Повторите ввод: ')
                                    self.spec[int(number) - 1].work_exp_min = float(work_exp)
                                    return
                                case '2':
                                    work_exp = input('Введите новый стаж работы: ')
                                    while not is_float(work_exp) or float(work_exp) < 0 or float(work_exp) > 100:
                                        work_exp = input('Некорректные данные. Стаж работы должен выглядеть как число от 0 (если его нет) до 100 (если он не важен). Повторите ввод: ')
                                    self.spec[int(number) - 1].work_exp_max = float(work_exp)
                                    return
                                case _:
                                    print('Команда не была распознана. Попытайтесь еще раз')
                    return
                case _:
                    print('Команда не была распознана. Попытайтесь еще раз')
