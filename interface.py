from list_of_specialization import List_of_specialization
from base import Base
from filter import Filter


class Interface:
    # Класс для взаимодействия - общения с пользователем. Так же именно он будет обрабатывать разного рода запросы
    # по изменению каким-то образом фильтра и иных вещей
    def __init__(self):
        # Конструктор для класса. Нам потребуется база данных, список всех профессий и фильтр
        self.all_spec = List_of_specialization()
        self.all_spec.read_from_file()
        self.data_base = Base()
        # ?? Какие параметры нужны для чтения из файла. (Например вроде нужен list_of_spec, так как  надо
        # почему-то проверять, что анкета хорошая или плохая)
        # self.data_base.read_from_file()
        self.filter = Filter()
