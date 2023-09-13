import pytest
from tdd.modules.osoba import Osoba

imena_osoba = [
    ("Ljuba", "Alicic"),
    ("Shemsa", "Suljakovic"),
    ("Toma", "Zdravkovic")
]

@pytest.mark.parametrize("ime,prezime", imena_osoba, ids=range(len(imena_osoba)))
def test_ime_prezime_01(ime, prezime):
    """
    Requirement: 01
    Osoba je definisana imenom i prezimenom
    Mocking:
    --------
        -
    :return:
    """
    o = Osoba(ime, prezime)
    assert hasattr(o, "ime")
    assert hasattr(o, "prezime")
    assert o.ime == ime
    assert o.prezime == prezime
