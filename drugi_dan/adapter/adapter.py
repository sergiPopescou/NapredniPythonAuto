from drugi_dan.adapter.ispis import Ispis
class Adapter(list):

    def __init__(self, objekat):
        super().__init__()
        self.append(Ispis("{"))
        for key in objekat.__dict__:
            self.append(Ispis(f'\t"{key}": "{objekat.__dict__[key]}",'))
        self.append(Ispis("}"))
