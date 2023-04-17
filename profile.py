

class Profile:
    # Это класс в котором будет храниться информация о профиле вакансии
    # или человека ищущего работу
    def __init__(self, name: str, placer: str, spec: list, salary: int, place_work: list, stars=None):
        # Это конструктор для класса Profile. name- ФИО, placer - разместитель объявления(компания или человек)
        # spec - специализация это будет лист в виде профессии и ее сужения
        # salary - зарплата, place_work - место где может работать(листом т.к. можно работать в разных городах)
        # stars - оценки (по умолчанию нет, но можно вписать как будто есть),
        # остается вопрос с отзывами о профиле(стоит ли делать?)

        self.name = name
        self.placer = placer
        self.spec = spec
        self.salary = salary
        self.place_work = place_work
        self.stars = stars

    def print_info(self):
        # Функция для вывода информации о профиле в консоль
        # Пока здесь будет заглушка !!!!! потом сделаем нормальную реализацию
        print(self.name)

    #def test_worthiness(self, filter: Filter) -> bool:
    # проверка на то, что профиль подходит под условия заданные пользователем(filter)
    # Пока опять же заглушка
