from profile import Profile
from specialization import Specialization
from list_of_specialization import List_of_specialization
from filter import Filter


class Base:
    # это база профилей(анкет), добавленных на сайт
    # Свободный id для новой анкеты
    data_base = []
    free_id = 0

    def add_new_profile(self, new_profile: Profile, list_of_spec: List_of_specialization) -> bool:
        # добавление нового профиля, если он пройдёт проверку
        if new_profile.check_all_spec_correct(list_of_spec):
            self.data_base.append(new_profile)
            self.free_id += 1
            return True
        else:
            with open('exeptions.txt', 'a') as exeption_file:
                exeption_file.write('Найден человек: ' + new_profile.name + 'с неопознанной специализацией' + '\n')
            return False

    def read_profile_from_file(self, list_of_spec: List_of_specialization):
        f_prof = open('input_file_of_profiles.txt')
        while f_prof.readline() != '':
            name = f_prof.readline()[: -1]
            placer = int(f_prof.readline()[: -1])
            buff = int(f_prof.readline())
            spec = []
            for i in range(buff):
                help_list = list(f_prof.readline()[: -1].split(', '))
                work_exp_min = float(f_prof.readline())
                work_exp_max = float(f_prof.readline())
                spec.append(Specialization(help_list, work_exp_min, work_exp_max))
            salary = float(f_prof.readline())
            buff = int(f_prof.readline())
            place_work = []
            for i in range(buff):
                place_work.append(f_prof.readline()[: -1])
            name_education = f_prof.readline()[: -1]
            level_education = int(f_prof.readline())
            buff = int(f_prof.readline())
            unique_skills = []
            for i in range(buff):
                unique_skills.append(f_prof.readline()[: -1])
            stars = list(map(int, f_prof.readline().split(', ')))
            new_prof = Profile(name, placer, spec, salary, place_work, name_education, level_education, unique_skills,
                               self.free_id, stars)
            self.add_new_profile(new_prof, list_of_spec)
        f_prof.close()

    def find_profile_by_id(self, new_id: int) -> int:
        # Функция находит по id индекс профиля в базе данных, если такого нет, то возвращает -1
        for prof in range(len(self.data_base)):
            if self.data_base[prof] == new_id:
                return prof

        return -1

    def delete_profile_by_id(self, new_id: int) -> bool:
        # Функция по выбранному id удаляет профиль в базе данных, если он там был и собственно сообщает о результате
        # в виде bool
        result = self.find_profile_by_id(new_id)
        if result == -1:
            return False
        else:
            self.data_base.pop(result)
            return True

    def sift(self, filter: Filter) -> 'Base':
        # просеивание базы данных для поиска подходящих анкет, функция возвращает новую, просеенную базу данных
        # если база данных получится пустая, то этот момент будет обработан при её получении
        sifted_data_base = Base()
        sifted_data_base.free_id = self.free_id
        for current_profile in self.data_base:
            if current_profile.test_worthiness(filter):
                sifted_data_base.data_base.append(current_profile)
        return  sifted_data_base

    def sort_data_base(self, filter: Filter) -> 'Base':
        # функция сортировки фильтра по определённому параметру,
        # параметр name - сортировка по имени, salary - сортировка по зарплате,
        # level_education - сортировка по уровню образования;
        # up - сортировка по возрастанию
        # down - сортировка по убыванию
        # в случае исключения ошибка будет выведена в exeption
        sorted_data_base = Base()
        match filter.parameter_of_sort:
            case 'name_up': sorted_data_base = sorted(self.data_base, key=lambda prof: prof.name)
            case 'name_down': sorted_data_base = sorted(self.data_base, key=lambda prof: prof.name, reverse=True)
            case 'salary_up': sorted_data_base = sorted(self.data_base, key=lambda prof: prof.salary)
            case 'salary_down': sorted_data_base = sorted(self.data_base, key=lambda prof: prof.salary, reverse=True)
            case 'level_education_up': sorted_data_base = sorted(self.data_base, key=lambda prof: prof.level_education)
            case 'level_education_down':
                sorted_data_base = sorted(self.data_base, key=lambda prof: prof.level_education, reverse=True)
            case _:
                with open('exeptions.txt', 'a') as exeption_file:
                    exeption_file.write('Некорректно введён параметр сортировки: \n')

        return sorted_data_base

    def sift_and_sort(self, filter: Filter) -> 'Base':
        # просеивание и сортировка базы данных, функция возвращает новую базу данных,
        # просеенную и отсортированную базу данных
        new_data_base = self.sift(filter)
        new_data_base.sort_data_base(filter)
        return new_data_base
