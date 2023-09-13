import random

from tdd.modules.osoba import Osoba


class OsobaUKancelariji(Osoba):
    def __init__(self, ime, prezime, moral=None):
        super().__init__(ime, prezime)
        self.posao = None
        if moral is None:
            self.calculateMoral()
        else:
            if not isinstance(moral, int):
                raise TypeError("Wrong type Moral")
            if moral < 0 or moral > 100:
                raise ValueError("Moral in range 0..100")
            self.moral = moral

    def addPosao(self, posao):
        self.posao = posao

    def calculateMoral(self):
        self.moral = random.randint(0, 100)
