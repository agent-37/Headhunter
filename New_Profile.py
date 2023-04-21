import Profile

def add_new_profile(self, name: str, placer: str, spec: list[Specialization], salary: int, place_work: list, \
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
