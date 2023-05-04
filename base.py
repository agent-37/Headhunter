from profile import Profile
from specialization import Specialization
from list_of_specialization import List_of_specialization


class Base:
    # это база профилей(анкет), добавленных на сайт
    # Свободный id для новой анкеты
    data_base = []
    free_id = 0

    def add_new_profile(self, new_profile: Profile, list_of_spec: List_of_specialization):
        # добавление нового профиля, если он пройдёт проверку
        if new_profile.check_all_spec_correct(list_of_spec):
            self.data_base.append(new_profile)
            self.free_id += 1
        else:
            with open('exeptions.txt', 'a') as exeption_file:
                exeption_file.write('Найден человек: ' + new_profile.name + 'с неопознанной специализацией' + '\n')

    def read_profile_from_file(self, list_of_spec: List_of_specialization):
        f_prof = open('input_file_of_profiles.txt')
        while f_prof.readline() != '':
            name = f_prof.readline()[: -1]
            placer = f_prof.readline()[: -1]
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
