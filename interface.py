from list_of_specialization import List_of_specialization
from base import Base
from filter import Filter


class Interface:
    # Класс для взаимодействия - общения с пользователем. Так же именно он будет обрабатывать разного рода запросы
    # по изменению каким-то образом фильтра и иных вещей
    def __init__(self):
        # Конструктор для класса. Нам потребуется база данных, список всех профессий и фильтр
        self.all_spec = List_of_specialization()
        self.data_base = Base()
        self.filter = Filter()

    def upload_base_from_file(self):
        self.data_base.read_profile_from_file(self.all_spec)

    def upload_spec_from_file(self):
        self.all_spec.read_from_file()

    def change_filter(self):
        # Функция для изменения пользователем фильтра.
        # Есть много проверок на дебила
        print('''Выбирите, как вы хотели бы изменить фильтр(введите цифру без точки)
                 1. Удалить все параметры фильтра
                 2. Изменить какой-то параметр
                 3. Показать установленные параметры фильтра
                 4. Выход''')
        while True:
            input_command = input()
            match input_command:
                case '1':
                    print('Вы точно уверены?(Введите 1 для подтверждения)')
                    del_answer = input()
                    if del_answer == '1':
                        self.filter.delete_all_info()
                case '2':
                    print('''Введите какой параметр поиска вы хотели бы изменить
                            1. ФИО или название организации
                            2. Соискатель или Работодатель
                            3. Специализации
                            4. Минимальная заработная плата
                            5. Максимальная заработная плата
                            6. Место работы
                            7. Уровень образования
                            8. Уникальные умения
                            9. Тип сортировки
                            10. Выход''')
                    input_command = input()
                    match input_command:
                        case '1': self.filter.change_name_from_console()
                        case '2': self.filter.change_placer_from_console()
                        case '3': self.filter.change_spec_from_console()
                        case '4': self.filter.change_min_salary_from_console()
                        case '5': self.filter.change_max_salary_from_console()
                        case '6': self.filter.change_place_work_from_console()
                        case '7': self.filter.change_level_education_from_console()
                        case '8': self.filter.change_unique_skills_from_console()
                        case '9': self.filter.change_parameter_of_sort_from_console()
                        case '10': break
                        case _: print('Команда не была распознана. Попытайтесь еще раз')
                case '3': self.filter.print_filter_info()
                case '4': break
                case _: print('Команда не была распознана. Попытайтесь еще раз')