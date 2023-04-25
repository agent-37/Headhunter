from specialization import Specialization

class List_of_specialization:
    specializations = []

    def add_specialization(self, new_spec: Specialization):
        # проверка на то, есть ли уже эта специализация в листе
        # !!здесь стоит сделать проверку на то, что специализыция введена корректно (под вопросом)
        if new_spec not in self.specializations:
            self.specializations.append(new_spec)
        # !!иначе ошибка (потом сделать или не сделать)

    def read_from_file(self):
        # чтение специализаций из файла
        with open('input_file.txt') as f_spec:
            file_str = f_spec.readline()
            self.add_specialization(Specialization(list(file_str.split())))
            while file_str:
                file_str = f_spec.readline()
                self.add_specialization(Specialization(list(file_str.split())))







