import pytest
from tdd.modules.klijent import Klijent, Annoying
from tdd.modules.projekat import Projekat
from tdd.modules.osoba import Osoba

imena_osoba = [
    ("Ime", "Semso")
]

@pytest.mark.parametrize("ime,prezime", imena_osoba)
def test_ime_prezime(ime, prezime):
    """
    Requirement 31:
    Klijent je Osoba

    :param ime:
    :param prezime:
    :return:
    """
    klijent = Klijent(ime, prezime)
    assert isinstance(klijent, Osoba)
    assert klijent.ime == ime
    assert klijent.prezime == prezime


@pytest.mark.parametrize("ime,prezime", imena_osoba)
def test_default_annoy(ime, prezime):
    """
    Requirement 32:
        Klijent definise defaultnu vrijednost za annoying. Defaultna vrijednost za annoying je Medium

    :param ime:
    :param prezime:
    :return:
    """
    klijent = Klijent(ime, prezime)
    assert hasattr(klijent, 'annoying')
    assert klijent.annoying is not None
    assert isinstance(klijent.annoying, Annoying)
    assert klijent.annoying == Annoying.Medium


imena_osoba_annoy = [
    ("Ime", "Semso", Annoying.Low),
    ("Ime", "Semso", Annoying.High),
    ("Ime", "Semso", Annoying.Medium),
    ("Pogresan", "Tip", "annoying"),
    ("Izvan", "Opsega", 333)
]


@pytest.mark.parametrize("ime,prezime,annoy", imena_osoba_annoy, ids=range(len(imena_osoba_annoy)))
def test_annoy(ime, prezime, annoy):
    """
    Requirement 32:
        Klijent moze opciono da definise vrijednost za annoying.
        Annoying ima jednu od vrijednosti : Low, Medium and High

    :param ime:
    :param prezime:
    :param annoy:
    :return:
    """
    if isinstance(annoy, Annoying):
        klijent = Klijent(ime, prezime, annoying=annoy)
        assert hasattr(klijent, 'annoying')
        assert klijent.annoying == annoy
        assert isinstance(klijent.annoying, Annoying)
    else:  # catch type exception
        with pytest.raises(TypeError):
            Klijent(ime, prezime, annoying=annoy)


@pytest.mark.parametrize("ime,prezime,annoy", imena_osoba_annoy[:3], ids=range(3))
def test_projekat(ime, prezime, annoy):
    """
    Requirement 33:
        Klijent ima Projekat.

    :param ime:
    :param prezime:
    :param annoy:
    :return:
    """
    klijent = Klijent(ime, prezime, annoying=annoy)
    assert hasattr(klijent, 'projekat')
    assert klijent.projekat == Projekat()
