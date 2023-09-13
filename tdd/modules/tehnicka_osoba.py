from tdd.modules.osoba_u_kancelariji import OsobaUKancelariji
from tdd.modules.issue import Issue

class TehnickaOsoba(OsobaUKancelariji):
    def __init__(self, ime, prezime, senioritet):
        super().__init__(ime, prezime)
        self.senioritet = senioritet

    def addPosao(self, posao):
        if not isinstance(posao, Issue):
            raise TypeError("Posao je Issue")
        # if self.posao is not None:
        #     self.posao.removeOsoba()
        self.posao = posao
        posao.addOsoba(self)

