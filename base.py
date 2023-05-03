from profile import Profile
from specialization import Specialization
from list_of_specialization import List_of_specialization


class Base:
    # это база профилей(анкет), добавленных на сайт
    data_base = []

    def add_new_profile(self, new_profile: Profile, list_of_spec: List_of_specialization):
        # добавление нового профиля, если он пройдёт проверку
        if new_profile.check_all_spec_correct(list_of_spec):
            self.data_base.append(new_profile)
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
                               stars)
            self.add_new_profile(new_prof, list_of_spec)
        f_prof.close()

