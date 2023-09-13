"""
41	OsobaUKncelariji je Osoba.
42	OsobaUKancelariji opciono definise vrijednost za moral. Moral ima cjelobrojnu vrijednosti u opsegu od 0 do 100
43	Ukoliko nije definisana vrijednost morala se dobija slučajno.
44	OsobaUKancelariji ima funkciju koja izračunava moral
45	OsobaUKancelariji ima posao, kao obavezan podatak
"""

import pytest
from tdd.modules.osoba_u_kancelariji import OsobaUKancelariji, Osoba


def test_je_osoba():
    """
    Requirement 41:
    	OsobaUKncelariji je Osoba.
    """
    assert isinstance(OsobaUKancelariji("ime", "prezime"), Osoba)


def test_moral_opciono():
    """
    Requirement 42:
        OsobaUKancelariji opciono definise vrijednost za moral. Moral ima cjelobrojnu vrijednosti u opsegu od 0 do 100
    """
    ouk = OsobaUKancelariji("ime", "prezime", moral=12)
    assert ouk.moral == 12
    with pytest.raises(TypeError):
        OsobaUKancelariji("ime", "prezime", moral="NotANumber")
    with pytest.raises(ValueError):
        OsobaUKancelariji("ime", "prezime", moral=101)
    with pytest.raises(ValueError):
        OsobaUKancelariji("ime", "prezime", moral=-1)


def test_moral_slucajan():
    """
    Requirement 43:
        Ukoliko nije definisana vrijednost morala se dobija slučajno.
    """
    ouk = OsobaUKancelariji("ime", "prezime")
    assert ouk.moral >= 0
    assert ouk.moral <= 100


def test_moral_calculator():
    """
    Requirement 44:
    	OsobaUKancelariji ima funkciju koja izračunava moral
    """
    assert hasattr(OsobaUKancelariji("ime", "prezime"), "calculateMoral")


def test_obavezan_posao():
    """
    Requirement 45:
    	OsobaUKancelariji ima posao, kao obavezan podatak
    """
    ouk = OsobaUKancelariji("ime", "prezime")
    assert hasattr(ouk, "posao")
    assert hasattr(ouk, "addPosao")
    ouk.addPosao("posao")
    assert ouk.posao == "posao"