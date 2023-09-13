from tdd.modules.osoba import Osoba, OsobaTypeError


class WrongNivoError(ValueError):
    """
    Error koji se podize kada nivo Issue-a nije dobar.
    """
    def __init__(self, nivo):
        super().__init__(f"Pogresan nivo {nivo}, dozvoljeni nivoi [{Issue._nivoi}]")


class StatusValueError(ValueError):
    """
    Error koji se podize kada nivo Issue-a nije dobar.
    """
    def __init__(self, status):
        super().__init__(f"Pogresan status {status}, dozvoljeni statusi [{Issue._statusi}]")


class StatusWorkflowError(ValueError):
    """
    Error koji se podize kada nivo Issue-a nije dobar.
    """
    def __init__(self, message):
        super().__init__(message)


class Issue:
    """
    Issue ima obavezne naziv i nivo
    Issue je dio projekta, a dodjeljuje se tehnickim osobama
    Attributes
    ----------
            naziv - string - naziv issuea
            nivo - ?
            status -
    """

    _nivoi = ("low", "medium", "high")
    """klasna varijabla mogucih nivoa"""

    _statusi = ("Open", "InProgress", "Closed")
    """klasna varijabla mogucih statusa"""

    def __init__(self, naziv, nivo):
        """
            nivo mora biti u skupu (low meidum)
            For example:
            >>> Issue("naziv", "low").nivo
            'low'
            >>> Issue("naziv", "medium").status
            'Open'
            >>> Issue("naziv", "high").naziv
            'naziv'

        :param naziv:
        :param nivo:
        """
        if not Issue._validanNivo(nivo):
            raise WrongNivoError(nivo)
        self.naziv = naziv
        self.nivo = nivo
        self.osoba = None
        self._status = "Open"

    @classmethod
    def _validanNivo(cls, nivo):
        """
        KLASNA funkcija provjerava da li je proslijedjeni parameter u skupu mogucih nivoa!
        :return:
        """
        # if isinstance(nivo, Nivo):
        # sada smo nezavisni od toga kako ce izgledati bilo kakva provjera.
        # ukoliko se nešto promijeni, samo ce se dirati ovaj metod.
        return nivo in Issue._nivoi

    def checkNivo(self, target_):
        """
        Funkcija koja provjerava da li je nivo Issue-a isti kao i dati nivo.
        Primjer:
        >>> Issue("naziv", "low").checkNivo("nepostojeci")
        False
        >>> Issue("naziv", "low").checkNivo("high")
        False
        >>> Issue("naziv", "high").checkNivo("high")
        True

        :param target_: ciljani nivo
        :return: bool -
        """
        if Issue._validanNivo(target_):
            return self.nivo == target_
        return False

    def addOsoba(self, osoba):
        """
        Funkcija koja dodaje Osobu na Issue
        Primjer:
        >>> Issue("naziv", "low").addOsoba(Osoba("ime", "prezime"))

        :param osoba: Osoba koja radi na Issue-u
        """
        if not isinstance(osoba, Osoba):
            raise OsobaTypeError()
        self.osoba = osoba

    def removeOsoba(self):
        """
        Funkcija koja oduzima Osobu sa Issue-a
        Primjer:
        >>> Issue("naziv", "low").removeOsoba()
        
        """
        if self.osoba is not None:
            self.osoba = None

    def __str__(self):
        """
        Stringovna reprezentacija objekta.
        Primjer:
        >>> str(Issue("naziv", "low"))
        'issue-naziv(low)'

        :return: str
        """
        return f"issue-{self.naziv}({self.nivo})"

    @property
    def status(self):
        """
        Property status
        Primjer:
        >>> Issue("naziv", "medium").status
        'Open'

        :return: str
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Seter statusa
        Primjer:
        >>> Issue("naziv", "medium").status = "Closed"

        :param value:
        :return:
        """
        if not Issue._validanStatus(value):
            raise StatusValueError(value)
        if self._status != value:
            # ovdje se sada moze dodati i dodatni uslov, kao sto je npr:
            # takodje iz statusa Closed se ne moze ici nigdje:
            if self._status == "Closed":
                raise StatusWorkflowError("u status Closed se moze doci samo preko InProgress")
            # status ne moze iz Open preci direktno u Closed, nego mora preko InProgres
            if value == "Closed" and self._status != "InProgress":
                raise StatusWorkflowError("u status Closed se moze doci samo preko InProgress")
            self._status = value

    @classmethod
    def _validanStatus(cls, status):
        """
        Klasna funkcija koja provjerava da li je status validan
        Primjeri:
        >>> Issue._validanStatus("ne postoji")
        False
        >>> Issue._validanStatus("Open")
        True

        :param status: str
        :return: bool
        """
        return status in Issue._statusi
