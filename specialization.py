

class Specialization:
    # Класс профессии. Состоит из списка для сужения специализации
    def __init__(self, profession: list[str], work_exp_min=None, work_exp_max=None):
        self.profession = profession
        self.work_exp_min = work_exp_min
        self.work_exp_max = work_exp_max

    def __eq__(self, other: 'Specialization'):
        # переопределил метод ==, так как in не работает
        if len(self.profession) != len(other.profession):
            return False
        for i in range(len(self.profession)):
            if self.profession[i] != other.profession[i]:
                return False
        return True

    def is_nested(self, new_profession: 'Specialization') -> bool:
        # Функция проверят вложена ли new_profession в данную profession
        # !! Тут стоит написать new_profession: Specialization, но PyCharm ругается поэтому пока будет без этого
        if len(new_profession.profession) > len(self.profession):
            return False
        if self.work_exp_min is not None and self.work_exp_min > new_profession.work_exp_min or \
                self.work_exp_max is not None and self.work_exp_max < new_profession.work_exp_max:
            return False
        for position in range(len(new_profession.profession)):
            if new_profession.profession[position] is not self.profession[position]:
                return False

        return True

    def reduce_spec(self) -> None:
        # Убирает элемент из профессии
        if len(self.profession) != 0:
            self.profession.pop()

