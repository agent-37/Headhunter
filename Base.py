import Profile


class Base:
    # это база профилей(анкет), добавленных на сайт
    data_base = []
    # это видимая(отфильтрованная) база профилей(анкет), добавленных на сайт и
    visible_data_base = []
    def add_new_profile(self, new_profile: Profile):
        # !!здесь стоит сделать проверку на то, что профиль хороший
        self.data_base.append(new_profile)
