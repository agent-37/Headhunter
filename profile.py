

class Profile:
    # Это класс в котором будет храниться информация о профиле вакансии
    # или человека ищущего работу
    def __init__(self, name: str, spec: list, salary: int, place_work: list, stars=None):
        # Это конструктор для класса Profile. name- ФИО, spec - специализация это будет лист из веточек дерева
        # salary - зарплата, place_work - место где может работать(листом т.к. можно работать в разных городах)
        # stars - оценочки(по умолчанию нету, но можно вписать как будто есть),
        # Остается вопрос с отзывами о профиле(стоит ли делать?)

        self.name = name
        self.spec = spec
        self.salary = salary
        self.place_work = place_work
        self.stars = stars

    def print_info(self):
        # Функия для вывода информации о профиле в консоль
        # Пока здесь будет заглушка !!!!! потом сделам нормальную реализацию
        print(self.name)

    #def test_worthiness(self, filter: Filter) -> bool:
    # проверка на то, что профиль подходит под условия заданные пользователем(filter)
    # Пока опять же заглушка
