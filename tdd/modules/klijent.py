import enum
from tdd.modules.osoba import Osoba
from tdd.modules.projekat import Projekat


class Annoying(enum.Enum):
    Low = 0
    Medium = 1
    High = 2


class Klijent(Osoba):
    """
    Klijent je osoba koja je vlasnik projekta i koja moze da utice na raspolozenje vodje projekta.
    Uticaj zavisi od annoying faktora
    Attributes
    ----------
            ime - string - naziv issuea
            prezime - ?
            annoying - Annoying

    """
    def __init__(self, ime, prezime, annoying=Annoying.Medium):
        """
        Konstruktor klijenta.
        Primjer:
        >>> Klijent("ime", "prezime").ime
        'ime'
        >>> Klijent("ime", "prezime").prezime
        'prezime'

        :param ime:
        :param prezime:
        :param annoying:
        """
        super().__init__(ime, prezime)
        if not isinstance(annoying, Annoying):
            raise TypeError("annoying is Annoying")
        self.annoying = annoying
        self.projekat = Projekat()
