import pytest
from tdd.modules.projekat import Projekat
from tdd.modules.issue import Issue
from tdd.modules.tehnicka_osoba import TehnickaOsoba

projekti = [
    ("Projekat1"),
    ("Projekat 2")
]


@pytest.fixture(scope="module")
def projekat_bez_issuea():
    """
    Fixture koji pravi projekat bez issuea
    :return:Projekat bez issuea
    """
    # kod za setup
    yield Projekat("naziv")
    # kod za teardown


@pytest.fixture(scope="function")
def projekat_sa_issueima():
    """
    Fixture koji pravi objekat projekta sa tri issuea.
    Svaki razlicitog prioriteta
    POSLIJE SVAKOG POZIVA TESTA SE RADI TEARDOWN
    :return: Projekat sa tri isuea
    """
    # kod za setup
    p = Projekat("naziv")
    p.addIssue(Issue("1", "low"))
    p.addIssue(Issue("2", "medium"))
    p.addIssue(Issue("3", "high"))
    yield p
    # kod za teardown
    p.issues = []

@pytest.fixture(scope="function")
def projekat_sa_issueima_i_osobama():
    """
    Fixture koji pravi objekat projekta sa tri issuea.
    Svaki razlicitog prioriteta, i svaki sa jednom tehnickom osobom

    :return: Projekat sa tri isuea
    """
    # kod za setup
    p = Projekat("naziv")
    i1 = Issue("1", "low")
    p.addIssue(i1)
    t = TehnickaOsoba("ime", "prezime", "junior")
    t.addPosao(i1)
    i2 = Issue("2", "medium")
    p.addIssue(i2)
    t = TehnickaOsoba("ime1", "prezime2", "medior")
    t.addPosao(i2)
    i3 = Issue("3", "high")
    p.addIssue(i3)
    t = TehnickaOsoba("ime3", "prezime4", "senior")
    t.addPosao(i3)
    yield p
    # kod za teardown
    p.issues = []


@pytest.fixture(scope="function")
def projekat_bez_issuea_sa_nazivom():
    """
    Fixture koji vraca FUNKCIJU koja kreita projekat promjenjivog naziva.
    :return: Funkcija
    """
    def projekat_(naziv):
        return Projekat(naziv)
    return projekat_


def test_default_naziv():
    """
    Requirement 11:
        Projekat ima naziv. ukoliko nije unesen zove se PROJEKAT
    """
    p = Projekat()
    assert hasattr(p, "naziv")
    assert p.naziv == "PROJEKAT"


@pytest.mark.parametrize("naziv", projekti, ids=range(len(projekti)))
def test_naziv(naziv, projekat_bez_issuea_sa_nazivom):
    """
    Requirement 11:
        Projekat ima naziv. ukoliko nije unesen zove se PROJEKAT
    """
    p = projekat_bez_issuea_sa_nazivom(naziv)
    assert hasattr(p, "naziv")
    assert p.naziv == naziv


def test_issuei(projekat_bez_issuea):
    """
    Requirement 12:
        Projekat sadrzi isuee, pocetno nema nijedan
    """
    p = projekat_bez_issuea
    assert hasattr(p, "issues")
    assert len(p.issues) == 0


@pytest.mark.parametrize("naziv", projekti, ids=range(len(projekti)))
def test_projekat_string(naziv):
    """
    Requirement: 13
        Projekat ima redefinisan stringovni prikaz. Format [NAZIV PROJEKTA]
    """
    p = Projekat(naziv)
    assert str(p) == f"[{naziv}]"


def test_pretraga_po_nivoima(projekat_sa_issueima):
    """
`   Requirement 14:
        Projekat ima mogućnost pretrage issuea po nivoima.

    :param projekat_sa_issueima: fixture
    """
    p = projekat_sa_issueima
    issues = list(p.filterIssuesByNivo("low"))
    assert len(issues) == 1
    assert issues[0].naziv == "1"
    issues = list(p.filterIssuesByNivo("medium"))
    assert len(issues) == 1
    assert issues[0].naziv == "2"
    issues = list(p.filterIssuesByNivo("high"))
    assert len(issues) == 1
    assert issues[0].naziv == "3"


def test_pretraga(projekat_sa_issueima_i_osobama):
    """
    Requirement 15:
        Projekat moze pronaci sve osobe koje rade na njemu.
    """
    projekat = projekat_sa_issueima_i_osobama
    assert hasattr(projekat, "getOsobeOnProjekt")
    osobe = projekat.getOsobeOnProjekt()
    assert len(osobe) == 3


def test_singleton():
    """
    Requirement 16:
        Projekat je singleton. Naziv se jedino mijenja
    :return:
    """
    p1 = Projekat("naziv1")
    p2 = Projekat("naziv1")
    assert p1 == p2
    assert p1.naziv == "naziv1"
    p3 = Projekat("drugi naziv")
    assert p1 == p3
    assert p1.naziv == "drugi naziv"


def test_named_issue(projekat_sa_issueima):
    """
    Requirement 17:
    	Projekat moze pretraziti issue po imenu (getIssueNamed)
    """
    assert hasattr(projekat_sa_issueima, "getIssueNamed")
    assert projekat_sa_issueima.getIssueNamed("not found") is None
    assert projekat_sa_issueima.getIssueNamed("1").naziv == "1"


def test_remove_named_issue(projekat_sa_issueima):
    """
    Requirement 18:
    	Projekat moze obrisati issue po imenu (removeIssueNamed)
    """
    assert hasattr(projekat_sa_issueima, "removeIssueNamed")
    assert len(projekat_sa_issueima.issues) == 3
    projekat_sa_issueima.removeIssueNamed("not found")
    assert len(projekat_sa_issueima.issues) == 3
    projekat_sa_issueima.removeIssueNamed("1")
    assert len(projekat_sa_issueima.issues) == 2
    assert projekat_sa_issueima.getIssueNamed("1") is None


def test_unique_issues():
    """
    Requirement 23:
    	Ne postoje dva issuea sa istim nazivom unutar projekta
    """
    p = Projekat()
    p.addIssue(Issue("1","low"))
    with pytest.raises(ValueError):
        p.addIssue(Issue("1","low"))
    p.removeIssueNamed("1")