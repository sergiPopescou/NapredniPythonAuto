class OsobaTypeError(TypeError):
    """
    Error koji se podize kada nivo Issue-a nije dobar.
    """
    def __init__(self):
        super().__init__("Osoba nije osoba")


class Osoba:
    """
    Osoba ima ime i prezime ...
    Primjer:
    >>> Osoba("ime", "prezime").ime
    'ime'
    >>> Osoba("ime", "prezime").prezime
    'prezime'
    """
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime

    def __str__(self):
        """
        Stringovna reprezentacija osobe IME_PREZIME

        :return: string
        """
        return f"{self.ime} {self.prezime}"
