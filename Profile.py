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

    def add_new_profile(self, name: str, placer: str, spec: list[Specialization], salary: int, place_work: list,\
                        stars=None) -> bool:
        # добавление нового профиля в Класс профессии (Specialization)
        # пока без полиморфизма, т.е. функция ждёт фиксированное число аргументов
        new_profile = Profile()
        new_profile.name = name
        new_profile.placer = placer
        new_profile.spec = spec
        new_profile.salary = salary
        new_profile.place_work = place_work
        new_profile.stars = stars
        # далее этот профиль отправляется в фильтр, но насколько я понимаю он пока не работает
        # в случае удачной фильтрации функция вернёт True, иначе False


        return False



    # уточнить:
    # лист специализации это список вакансий на сайте или список прошлых работ безработного бедолаги
    # чё такое placer

    profile_list = []
    # скорее всего здесь будет более сложная реализация, чем просто список
