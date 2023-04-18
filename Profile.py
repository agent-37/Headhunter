import Filter
import Specialization


class Profile:
    # Это класс в котором будет храниться информация о профиле вакансии
    # или человека ищущего работу
    def __init__(self, name: str, placer: str, spec: list[Specialization], salary: int, place_work: list, stars=None):
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

    def test_worthiness(self, filter: Filter) -> bool:
        # проверка на то, что профиль подходит под условия заданные пользователем(filter)
        if filter.check_correct() is not True:
            return False
        if filter.name is not None and filter.name != self.name \
           or filter.placer is not None and filter.placer != self.placer \
           or filter.min_salary is not None and filter.min_salary > self.salary\
           or filter.max_salary is not None and filter.max_salary < self.salary\
           or filter.place_work is not None and filter.place_work not in self.place_work:
            return False

        if filter.spec is not None:
            for one_spec in self.spec:
                if filter.spec.is_nested(one_spec):
                    return True

        return False
