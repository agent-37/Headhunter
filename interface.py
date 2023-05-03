from list_of_specialization import List_of_specialization
from base import Base
from filter import Filter


class Interface:
    # Класс для взаимодействия - общения с пользователем. Так же именно он будет обрабатывать разного рода запросы
    # по изменению каким-то образом фильтра и иных вещей
    def __init__(self):
        # Конструктор для класса. Нам потребуется база данных, список всех профессий и фильтр
        self.all_spec = List_of_specialization()
        self.data_base = Base()
        self.filter = Filter()

    def upload_base_from_file(self):
        self.data_base.read_profile_from_file(self.all_spec)

    def upload_spec_from_file(self):
        self.all_spec.read_from_file()
