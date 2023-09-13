from drugi_dan.proxy.issue import Issue
from drugi_dan.proxy.osoba import Person, Seniority
class OsobaProxy:
    def __init__(self, name, seniority):
        self.osoba = Person(name, seniority)

    def addIssue(self, issue):
        if self.osoba.seniority == Seniority.JUNIOR and issue.difficulty == "HARD":
            print(f"Issue {issue} cannot be assigned to person, due to difficulty")
            return
        self.osoba.addIssue(issue)


if __name__ == '__main__':
    senior = OsobaProxy('Aleksa', Seniority.SENIOR)
    junior = OsobaProxy("Mane", Seniority.JUNIOR)
    hardIssue = Issue(123, "HARD")
    easyIssue = Issue(124, "EASY")
    junior.addIssue(hardIssue)
    print("junior issue after adding:", junior.osoba.issue)
    senior.addIssue(hardIssue)
    junior.addIssue(easyIssue)
    print("junior issue after adding easy one:", junior.osoba.issue)