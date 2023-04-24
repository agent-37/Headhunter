import Specialization

class List_of_specialization:
    specializations = []

    def add_specialization(self, new_spec: Specialization):
        # проверка на то, есть ли уже эта специализация в листе
        # !!здесь стоит сделать проверку на то, что специализыция введена корректно (под вопросом)
        if new_spec not in self.specializations:
            self.specializations.append(new_spec)
        # !!иначе ошибка (потом сделать или не сделать)

    def read_from_file:
        # чтение специализаций из файла
        f = open(input_file)





