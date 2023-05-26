from specialization import Specialization
from list_of_specialization import  List_of_specialization
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

class Filter:
    # Это класс в котором будет храниться информация о фильтре для отсеивания нужных и не нужных людей
    # Параметры в фильтре такие же как и в анкете, но часть из них может отсутствовать или быть не полной
    # Так же скажу, что setter и getter для переменных не имеет смысла делать, потому что легче сделать их публичными
    # parameter_of_sort - это тип сортировок
    name = None
    placer = None
    spec = None
    min_salary = None
    max_salary = None
    place_work = None
    level_education = None
    unique_skills = None
    parameter_of_sort = 'name_up'

    def add_spec(self, new_spec: str) -> None:
        # Добавляет элемент в специализацию для фильтра
        if self.spec is None:
            self.spec = [new_spec]
        else:
            self.spec.append(new_spec)

    def reduce_spec(self) -> None:
        # Убирает элемент из специализации для фильтра
        if self.spec is not None:
            self.spec.reduce_spec()

    def delete_all_info(self) -> None:
        # Удаляет всю информации из фильтра, просто упрощение, чтобы не удалять все вручную
        self.name = None
        self.placer = None
        self.spec = None
        self.min_salary = None
        self.max_salary = None
        self.place_work = None
        self.level_education = None
        self.unique_skills = None

    def check_correct(self) -> bool:
        # Проверка на корректность фильтра, то есть на минимальную информацию для просеивания информации
        if self.placer is not None and self.spec is not None:
            return True
        else:
            return False

    def print_filter_info(self):
        # Функция выводит информацию о фильтре
        if self.name is not None:
            print('ФИО или название работодателя:' + self.name)
        if self.placer is not None:
            if self.placer == 1:
                print('Работодатель')
            if self.placer == 0:
                print('Соискатель')
        if self.spec is not None:
            print('Специализация:', end=' ')
            self.spec.print_specialization()
        if self.min_salary is not None:
            print('Минимальная заработная плата:', self.min_salary)
        if self.max_salary is not None:
            print('Минимальная заработная плата:', self.max_salary)
        if self.place_work is not None:
            print('Город:', self.place_work)
        if self.level_education is not None:
            print('Уровень образования:', self.level_education)
        if self.unique_skills is not None:
            print('Особые умения')
            for skill in self.unique_skills:
                print(skill)
        print('Тип сортировки:', end='')
        match self.parameter_of_sort:
            case 'name_up': print('по возрастанию имени')
            case 'name_down': print('по убыванию имени')
            case 'salary_up': print('по возрастанию заработной платы')
            case 'salary_down': print('по убыванию заработной платы')
            case 'level_education_up': print('по возрастанию уровня образования')
            case 'level_education_down': print('по убыванию уровня образования')
            case _:
                with open('exeptions.txt', 'a') as exeption_file:
                    exeption_file.write('Некорректно обработан параметр сортировки при выводе фильтра \n')
        if not self.check_correct():
            print('Введенной информации не достаточно для нахождения анкет.')
            print('Убедитесь, что ввели параметры работодатель-соискатель и специализации')

    def change_name_from_console(self):
        # Функция смены имени с консоли
        while True:
            print('1. Удаление ФИО или название организации', '2. Изменение ФИО или названия организации',
                  '3. Показать ФИО или название организации', '4. Выход', sep='\n')
            console_input = input()
            match console_input:
                case '1': self.name = None
                case '2': self.name = input('Введите ФИО или название организации')
                case '3':
                    if self.name is None:
                        print('ФИО или названия организации не выбрано')
                    else:
                        print('ФИО или названия организации:', self.name)
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_placer_from_console(self):
        # Функция смены placer с консоли
        while True:
            print('1. Удаление работодатель-соискатель', '2. Изменение работодатель-соискатель',
                  '3. Показать работодатель-соискатель', '4. Выход', sep='\n')
            console_input = input()
            match console_input:
                case '1': self.placer = None
                case '2':
                    while True:
                        console_input = input()
                        match console_input:
                            case '0': self.placer = int(console_input)
                            case '1': self.placer = int(console_input)
                            case _: print('Команда не была распознана. Попытайтесь еще раз')
                case '3':
                    if self.placer is None:
                        print('Работодатель-соискатель не выбрано')
                    elif self.placer == 0:
                        print('Cоискатель')
                    else:
                        print('Работодатель')
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_min_salary_from_console(self):
        # Функция смены минимальной зп с консоли
        while True:
            print('1. Удаление параметра минимальной заработной платы',
                  '2. Изменение параметра минимальной заработной платы', '3. Показать минимальную заработную плату',
                  '4. Выход', sep='\n')
            console_input = input()
            match console_input:
                case '1': self.min_salary = None
                case '2':
                    while True:
                        console_input = input('Введите минимальную заработной платы')
                        if not is_float(console_input):
                            print('Минимальная заработная плата это вещественное число')
                            continue
                        console_input = float(console_input)
                        if console_input <= 0:
                            print('Минимальная заработная плата должна быть положительной')
                            continue
                        if self.max_salary is not None and console_input > self.max_salary:
                            print('Минимальная заработная плата должна быть не больше максимальной')
                            continue
                        break
                    self.min_salary = console_input
                case '3':
                    if self.min_salary is None:
                        print('Минимальная заработная плата не выбрана')
                    else:
                        print('Минимальная заработная плата', self.min_salary)
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_max_salary_from_console(self):
        # Функция смены максимальной зп с консоли
        while True:
            print('1. Удаление параметра максимальной заработной платы',
                  '2. Изменение параметра максимальной заработной платы', '3. Показать максимальную заработную плату',
                  '4. Выход', sep='\n')
            console_input = input()
            match console_input:
                case '1': self.max_salary = None
                case '2':
                    while True:
                        console_input = input('Введите минимальную заработной платы')
                        if not is_float(console_input):
                            print('Максимальная заработная плата это вещественное число')
                            continue
                        console_input = float(console_input)
                        if console_input <= 0:
                            print('Максимальная заработная плата должна быть положительной')
                            continue
                        if self.min_salary is not None and self.min_salary > console_input:
                            print('Минимальная заработная плата должна быть не больше максимальной')
                            continue
                        break
                    self.max_salary = console_input
                case '3':
                    if self.max_salary is None:
                        print('Максимальная заработная плата не выбрана')
                    else:
                        print('Максимальная заработная плата', self.max_salary)
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_place_work_from_console(self):
        # Функция смены места работы с консоли
        while True:
            print('1. Удаление места работы', '2. Изменение места работы', '3. Показать место работы', '4. Выход',
                  sep='\n')
            console_input = input()
            match console_input:
                case '1': self.place_work = None
                case '2': self.name = input('Введите место работы')
                case '3':
                    if self.place_work is None:
                        print('Место работы не выбрано')
                    else:
                        print('Место работы:', self.place_work)
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_level_education_from_console(self):
        # Функция смены места работы с консоли
        while True:
            print('1. Удаление уровня образования', '2. Изменение уровня образования',
                  '3. Показать уровень образования',
                  '4. Выход', sep='\n')
            console_input = input()
            match console_input:
                case '1': self.level_education = None
                case '2':
                    while True:
                        console_input = input('Введите уровень образования')
                        if not is_int(console_input):
                            print('Нужно ввести целое число от 0 до 6')
                            continue
                        console_input = int(console_input)
                        if console_input < 0 or console_input > 6:
                            print('Нужно ввести число от 0 до 6')
                            continue
                        break
                    self.level_education = console_input
                case '3':
                    if self.level_education is None:
                        print('Уровень образования не выбран')
                    else:
                        print('Уровень образования :', self.level_education)
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_unique_skills_from_console(self):
        # Функция изменения особых умений
        while True:
            print('1. Удаление всех особых умений', '2. Удаление одного особого умения', '3. Добавление умения',
                  '4. Показать особые умения', '5. Выход', sep='\n')
            console_input = input()
            match console_input:
                case '1': self.unique_skills = None
                case '2':
                    if self.unique_skills is None:
                        print('Особых умений нет')
                        continue
                    while True:
                        console_input = input('Введите номер удаляемого объекта')
                        if not is_int(console_input):
                            print('Введите целое положительное число')
                            continue
                        console_input = int(console_input)
                        if console_input < 1 or console_input > len(self.unique_skills):
                            print('Введите целое положительное число из диапазона')
                            continue
                        break
                    self.unique_skills.pop(console_input - 1)
                    if len(self.unique_skills) == 0:
                        self.unique_skills = None
                case '3':
                    if self.unique_skills is None:
                        self.unique_skills = [input('Введите особое умение')]
                    else:
                        self.unique_skills.append(input('Введите особое умение'))
                case '4':
                    if self.unique_skills is None:
                        print('Особые умения не выбраны')
                    else:
                        print('Особые умения:')
                        for skill in self.unique_skills:
                            print(skill)
                case '5': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_parameter_of_sort_from_console(self):
        # Функция изменения сортировки
        while True:
            print('1. По возрастанию имен', '2. По убыванию имен', '3. По возрастанию заработной платы',
                  '4. По убыванию заработной платы', '5. По возрастанию уровня образования',
                  '6. По убыванию уровня образования', '7. Показать тип сортировки', '8. Выход',
                  sep='\n')
            console_input = input()
            match console_input:
                case '1': self.parameter_of_sort = 'name_up'
                case '2': self.parameter_of_sort = 'name_down'
                case '3': self.parameter_of_sort = 'salary_up'
                case '4': self.parameter_of_sort = 'salary_down'
                case '5': self.parameter_of_sort = 'level_education_up'
                case '6': self.parameter_of_sort = 'level_education_down'
                case '7':
                    print('Тип сортировки:', end='')
                    match self.parameter_of_sort:
                        case 'name_up': print('по возрастанию имени')
                        case 'name_down': print('по убыванию имени')
                        case 'salary_up': print('по возрастанию заработной платы')
                        case 'salary_down': print('по убыванию заработной платы')
                        case 'level_education_up': print('по возрастанию уровня образования')
                        case 'level_education_down': print('по убыванию уровня образования')
                        case _:
                            with open('exeptions.txt', 'a') as exeption_file:
                                exeption_file.write('Некорректно обработан параметр сортировки при изменении фильтра\n')
                case '8': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_spec_from_console(self, list_of_spec: List_of_specialization):
        # Функция изменения сортировки
        while True:
            print('1. Удалить специализацию', '2.уточнить специализацию', '3. Показать текущую специализацию',
                  '4. Выход', sep='\n')
            console_input = input()
            match console_input:
                case '1': self.spec = None
                case '2':
                    local_spec = Specialization([''])
                    if self.spec is not None:
                        local_spec = self.spec
                    chosen_spec = list_of_spec.reduce_find_recommand(local_spec)
                    if len(chosen_spec) == 0:
                        print('Уточнее сделать не возможно')
                    else:
                        print('Возможные уточнения:')
                        for pos in chosen_spec:
                            print(pos)
                    while True:
                        console_input = input()
                        if console_input in chosen_spec:
                            local_spec.profession.append(console_input)
                            self.spec = local_spec
                            break
                        else:
                            print('Не распознанное уточнение. Попытайтесь еще раз')
                case '3':
                    if self.spec is None:
                        print('Специализация не выбрана')
                    else:
                        print('Специализация:', end='')
                        self.spec.print_specialization()
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')
