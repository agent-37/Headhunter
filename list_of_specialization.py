from specialization import Specialization

class List_of_specialization:
    specializations = []

    def add_specialization(self, new_spec: Specialization):
        # проверка на то, есть ли уже эта специализация в листе
        # !!здесь стоит сделать проверку на то, что специализация введена корректно (под вопросом)
        if new_spec not in self.specializations:
            self.specializations.append(new_spec)
        else:
            with open('exeptions.txt', 'a') as exeption_file:
                exeption_file.write('Найдена специализация, которая ранее уже была добавлена: '
                                    + str(new_spec.profession) + '\n')

    def read_from_file(self):
        # чтение специализаций из файла с проверкой повторений
        with open('input_file_of_specialization.txt') as f_spec:
            file_str = f_spec.readline()
            self.add_specialization(Specialization(list(file_str.split(', '))))
            while file_str:
                file_str = f_spec.readline()
                self.add_specialization(Specialization(list(file_str.split(', '))))

