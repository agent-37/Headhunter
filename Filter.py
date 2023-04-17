

class Filter:
    # Это класс в котором будет храниться информация о фильтре для отсеивания нужных и не нужных людей
    # Параметры в фильтре такие же как и в анкете, но часть из них может отсутствовать или быть не полной
    # Так же скажу, что setter и getter для переменных не имеет смысла делать, потому что легче сделать их публичными
    name = None
    placer = None
    spec = None
    salary = None
    place_work = None
    stars = [0, 0, 0, 0, 0]

    def add_spec(self, new_spec: str) -> None:
        # Добавляет элемент в специализацию для фильтра
        if self.spec is None:
            self.spec = [new_spec]
        else:
            self.spec.append(new_spec)

    def reduce_spec(self) -> None:
        # Убирает элемент из специализации для фильтра
        if self.spec is not None:
            self.spec.pop()

    def delete_all_info(self) -> None:
        # Удаляет всю информации из фильтра, просто упрощение, чтобы не удалять все вручную
        self.name = None
        self.placer = None
        self.spec = None
        self.salary = None
        self.place_work = None
        self.stars = [0, 0, 0, 0, 0]

    def check_correct(self) -> bool:
        # Проверка на корректность фильтра, то есть на минимальную информацию для просеивания информации
        if self.placer is not None and self.spec is not None:
            return True
        else:
            return False
