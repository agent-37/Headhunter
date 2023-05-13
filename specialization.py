

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
        if len(new_profession.profession) > len(self.profession):
            return False
        for position in range(len(new_profession.profession)):
            if new_profession.profession[position] != self.profession[position]:
                return False

        return True

    def reduce_spec(self) -> None:
        # Убирает элемент из профессии
        if len(self.profession) != 0:
            self.profession.pop()

    def print_specialization(self):
        for position in range(len(self.profession)-1):
            print(self.profession[position], end=', ')
        print(self.profession[-1])
