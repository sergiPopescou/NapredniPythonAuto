from drugi_dan.mediator.issue import Issue
from drugi_dan.mediator.tehnicka_osoba import TehnickaOsoba

if __name__ == '__main__':
    issue1 = Issue(1)

    dane = TehnickaOsoba('Dane')
    mane = TehnickaOsoba('Mane')
    mitar = TehnickaOsoba('Mitar')

    issue1.join(dane)
    issue1.join(mane)

    mane.postReview(issue1, "ovo ti nista ne valja")
    dane.postReview(issue1, "kako ne valja")

    issue1.join(mitar)
    mane.postReview(issue1, "nemoj se ljutiti na mene")