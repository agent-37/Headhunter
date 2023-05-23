from specialization import Specialization


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
        print('''1. Удаление ФИО или название организации
                 2. Изменение ФИО или названия организации
                 3. Выход''')
        while True:
            console_input = input()
            match console_input:
                case '1': self.name = None
                case '2': self.name = input('Введите ФИО или название организации')
                case '3': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')

    def change_placer_from_console(self):
        # Функция смены placer с консоли
        print('''1. Удаление работодатель-соискатель
                 2. Изменение работодатель-соискатель
                 3. Выход''')
        while True:
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
                case '3': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')