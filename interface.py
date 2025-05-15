from list_of_specialization import List_of_specialization
from base import Base
from filter import Filter
from profile import Profile, is_int


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


    def change_filter(self, list_of_spec: List_of_specialization):
        # Функция для изменения пользователем фильтра.
        # Есть много проверок на дебила
        while True:
            print('Выберите, как вы хотели бы изменить фильтр(введите цифру без точки)',
                  '1. Удалить все параметры фильтра',
                  '2. Изменить какой-то параметр', '3. Показать установленные параметры фильтра', '4. Выход', sep='\n')
            input_command = input('Выберите пункт: ')
            match input_command:
                case '1':
                    print('Вы точно уверены?(Введите 1 для подтверждения)')
                    del_answer = input('Выберите пункт: ')
                    if del_answer == '1':
                        self.filter.delete_all_info()
                case '2':
                    print('Введите какой параметр поиска вы хотели бы изменить', '1. ФИО или название организации',
                          '2. Соискатель или Работодатель', '3. Специализации', '4. Минимальная заработная плата',
                          '5. Максимальная заработная плата', '6. Место работы', '7. Уровень образования',
                          '8. Уникальные умения', '9. Тип сортировки', '10. Выход', sep='\n')
                    input_command = input('Выберите пункт: ')
                    match input_command:
                        case '1': self.filter.change_name_from_console()
                        case '2': self.filter.change_placer_from_console()
                        case '3': self.filter.change_spec_from_console(list_of_spec)
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

    def add_profile_in_data_base_from_console(self):
        # функция добавляет прочитанный с консоли профиль в data_dase
        print('Заполните анкету: ')
        new_prof = Profile()
        new_prof.read_from_console(self.all_spec)
        if not self.data_base.add_new_profile(new_prof, self.all_spec):
            print('Что-то пошло не так, профиль не добавлен')

    def delete_profile_from_data_base(self):
        # функция удаляет профиль из базы данных по введённой позиции
        num = input('Введите номер позиции профиля: ')
        visible_base = self.data_base.sift_and_sort(self.filter)
        if len(visible_base.data_base) == 0:
            print('Список анкет пуст ')
            return
        while not is_int(num) or 0 >= int(num) or int(num) > len(visible_base.data_base):
            num = input('Введите корректный номер позиции профиля: ')
        self.data_base.delete_profile_by_id(visible_base.data_base[int(num)-1].id)

    def open_and_interaction_profile(self):
        # функция открывает профиль для просмотра и взаимодействия с пользователем
        num = input('Введите номер позиции профиля: ')
        visible_base = self.data_base.sift_and_sort(self.filter)
        if len(visible_base.data_base) == 0:
            print('Список анкет пуст ')
            return
        while not is_int(num) or 0 >= int(num) or int(num) > len(visible_base.data_base):
            num = input('Введите корректный номер позиции профиля: ')
        visible_base.data_base[int(num) - 1].print_all_info()
        while True:
            print('Выберите действие для данного профиля',
                  '1. Удаление профиля', '2. Изменение профиля', '3. Добавление звёздочки профилю',
                  '4. Снова показать профиль', '5. Выход', sep='\n')
            console_input = input('Выберите пункт: ')
            match console_input:
                case '1':
                    self.data_base.delete_profile_by_id(visible_base.data_base[int(num) - 1].id)
                    break
                case '2':
                    self.data_base.data_base[self.data_base.find_profile_by_id(visible_base.data_base[int(num) - 1].id)].change_profile()
                case '3':
                    if self.data_base.data_base[self.data_base.find_profile_by_id(visible_base.data_base[int(num) - 1].id)].feedback_added:
                        print('Отзыв уже добавлен ')
                        continue
                    console_input = input('Введите, к какой позиции хотели бы добавить звездочку:\n')
                    while not is_int(console_input) or 0 >= int(console_input) or int(console_input) > 5:
                        console_input = input('Введите корректный номер позиции профиля: ')
                    self.data_base.data_base[self.data_base.find_profile_by_id(visible_base.data_base[int(num) - 1].id)].stars.append(int(console_input))
                    self.data_base.data_base[
                         self.data_base.find_profile_by_id(visible_base.data_base[int(num) - 1].id)].feedback_added = 1
                case '4':
                    visible_base.data_base[int(num) - 1].print_all_info()
                case '5':
                    break
                case _:
                    print('Команда не была распознана. Попытайтесь еще раз')

    def change_profile_from_data_base(self):
        # функция интерфейса для изменения профиля
        num = input('Введите номер позиции профиля: ')
        visible_base = self.data_base.sift_and_sort(self.filter)
        if len(visible_base.data_base) == 0:
            print('Список анкет пуст ')
            return
        while not is_int(num) or 0 >= int(num) or int(num) > len(visible_base.data_base):
            num = input('Введите корректный номер позиции профиля: ')
        self.data_base.data_base[self.data_base.find_profile_by_id(visible_base.data_base[int(num) - 1].id)].change_profile(self.all_spec)

    def interact_with_user(self):
        # главная функция интерактива с пользователем
        self.upload_spec_from_file()
        self.upload_base_from_file()
        print('Привет, пользователь. Ты находишься на лучшем сайте по поиску работы \'Охотник за головами\'.')
        while True:
            if not self.filter.check_correct():
                print('В фильтре необходимо выбрать специализацию и параметр работодатель-соискатель.')
                print('1. Изменить фильтр', '2. Добавить профиль в базу данных', '3. Выход', sep='\n')
                number = input('Выберите пункт: ')
                match number:
                    case '1': self.change_filter(self.all_spec)
                    case '2': self.add_profile_in_data_base_from_console()
                    case '3': return
                    case _: print('Команда не была распознана. Попытайтесь еще раз')
            else:
                visible_base = self.data_base.sift_and_sort(self.filter)
                if len(visible_base.data_base) == 0:
                    print('Вы использовали слишком жесткий фильтр. По вашему запросу не было ничего найдено')
                    print('1. Изменить фильтра', '2. Добавить профиль в базу данных', '3. Выход', sep='\n')
                    number = input('Выберите пункт: ')
                    match number:
                        case '1':
                            self.change_filter(self.all_spec)
                        case '2':
                            self.add_profile_in_data_base_from_console()
                        case '3':
                            return
                        case _:
                            print('Команда не была распознана. Попытайтесь еще раз')
                else:
                    print('Возможные действия:', '1. Изменить фильтр', '2. Добавить профиль в базу данных',
                          '3. Удалить профиль из базы данных', '4. Открыть профиль для просмотра',
                          '5. Изменить профиль', '6. Выйти', sep='\n')
                    visible_base.print_base()
                    number = input('Выберите пункт: ')
                    match number:
                        case '1': self.change_filter(self.all_spec)
                        case '2': self.add_profile_in_data_base_from_console()
                        case '3': self.delete_profile_from_data_base()
                        case '4': self.open_and_interaction_profile()
                        case '5': self.change_profile_from_data_base()
                        case '6':
                            print('До свидания. Мы будем рады снова увидеть вас на нашем сайте.')
                            return
                        case _: print('Команда не была распознана. Попытайтесь еще раз')
