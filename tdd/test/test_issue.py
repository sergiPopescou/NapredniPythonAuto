import pytest
from tdd.modules.issue import Issue
from tdd.modules.osoba import Osoba


def test_naziv():
    """
    Requirement 21:
    Issue ima obavezan naziv i nivo
    :return:
    """
    with pytest.raises(TypeError):
        Issue("naziv")
    with pytest.raises(TypeError):
        Issue("q", "3", "fff")
    p = Issue("naziv", "med")
    assert hasattr(p, "naziv")
    assert hasattr(p, "nivo")
    assert p.naziv == "naziv"
    assert p.nivo == "med"


def test_nivo():
    """
    Requirement 22:
        Nivo issuea moze biti: Low, Medium, High
    """
    with pytest.raises(ValueError):
        Issue("neziv", "low1")
    for n in ("low", "med", "high"):
        i = Issue("neziv", n)
        assert i.nivo == n


def test_add_osoba():
    """
    Requirement 15:
        Za potrebe ovog zahtjeva issue treba da ima add_osoba()
    """
    i = Issue("naziv", "low")
    assert hasattr(i, "addOsoba")
    assert i.osoba is None
    i.addOsoba(Osoba("ime", "prezime"))
    assert i.osoba.ime == "ime"
    assert i.osoba.prezime == "prezime"
    with pytest.raises(TypeError):
        i.addOsoba("Nesto")


def test_remove_osoba():
    """
    Requirement 15:
        Za potrebe ovog zahtjeva issue treba da ima removeOsoba()
    """
    i = Issue("naziv", "low")
    assert hasattr(i, "removeOsoba")
    assert i.osoba is None
    i.removeOsoba()
    assert i.osoba is None
    i.addOsoba(Osoba("ime", "prezime"))
    assert i.osoba.ime == "ime"
    assert i.osoba.prezime == "prezime"
    i.removeOsoba()
    assert i.osoba is None


def test_str():
    """
    Requirement 24:
    	Issue ima redefinisan stringovni prikaz. FORMAT: [issue-NAZIV(nivo)]
    """
    i = Issue("naziv", "low")
    assert str(i) == f"issue-{i.naziv}({i.nivo})"


def test_status():
    """
    Requirement 25:
    	Issue ima status: Open, InProgress, Closed
    Requirement 26:
        Uobicajeni status je Open
    """
    i = Issue("naziv", "low")
    assert hasattr(i, "status")
    assert i.status == "Open"
    i.status = "InProgress"
    assert i.status == "InProgress"
    with pytest.raises(ValueError):
        i.status = "nepostojeci"
