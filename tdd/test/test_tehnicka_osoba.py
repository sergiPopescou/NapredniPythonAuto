from tdd.modules.issue import Issue
from tdd.modules.tehnicka_osoba import TehnickaOsoba

class MockIssue(Issue):

    def __init__(self, naziv, nivo):
        self.addOsoba_call_count = 0

    def addOsoba(self, osoba):
        self.addOsoba_call_count += 1


def test_posao_je_issue():
    """
    Requirement 74:
        Posao TehnickaOsoba je Issue
    :return:
    """
    t = TehnickaOsoba("ime", "prezime", "senior")
    m = MockIssue("issue", "low")
    t.addPosao(m)
    assert isinstance(t.posao, Issue)
    assert m.addOsoba_call_count == 1