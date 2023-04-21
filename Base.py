import Profile
import Specialization


class Base:
    # это база профилей(анкет), добавленных на сайт
    data_base = []
    visible_data_base = []
    def add_new_profile(self, name: str, placer: str, spec: list[Specialization], salary: int, place_work: list, \
                        stars=None) -> bool:
        new_profile = Profile(name, placer, spec, salary, place_work, stars)
        data_base.append(new_profile)







