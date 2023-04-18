

class Specialization:
    # Класс профессии. Состоит из списка для сужения специализации
    def __init__(self, profession: list[str]):
        self.profession = profession

    def is_nested(self, new_profession) -> bool:
        # Функция проверят вложена ли new_profession в данную profession
        # !! Тут стоит написать new_profession: Specialization, но PyCharm ругается поэтому пока будет без этого
        if len(new_profession.profession) > len(self.profession):
            return False

        for position in range(len(new_profession.profession)):
            if new_profession.profession[position] is not self.profession[position]:
                return False

        return True

    def reduce_spec(self) -> None:
        # Убирает элемент из профессии
        if len(self.profession) != 0:
            self.profession.pop()
