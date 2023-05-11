from specialization import Specialization


class Filter:
    # Это класс в котором будет храниться информация о фильтре для отсеивания нужных и не нужных людей
    # Параметры в фильтре такие же как и в анкете, но часть из них может отсутствовать или быть не полной
    # Так же скажу, что setter и getter для переменных не имеет смысла делать, потому что легче сделать их публичными
    # kind_of_sort - это тип сортировок
    name = None
    placer = None
    spec = None
    min_salary = None
    max_salary = None
    place_work = None
    level_education = None
    unique_skills = None
    parameter_of_sort = 'name_up'

    def add_spec(self, new_spec: str) -> None:
        # Добавляет элемент в специализацию для фильтра
        if self.spec is None:
            self.spec = [new_spec]
        else:
            self.spec.append(new_spec)

    def reduce_spec(self) -> None:
        # Убирает элемент из специализации для фильтра
        if self.spec is not None:
            self.spec.reduce_spec()

    def delete_all_info(self) -> None:
        # Удаляет всю информации из фильтра, просто упрощение, чтобы не удалять все вручную
        self.name = None
        self.placer = None
        self.spec = None
        self.min_salary = None
        self.max_salary = None
        self.place_work = None
        self.level_education = None
        self.unique_skills = None

    def check_correct(self) -> bool:
        # Проверка на корректность фильтра, то есть на минимальную информацию для просеивания информации
        if self.placer is not None and self.spec is not None:
            return True
        else:
            return False