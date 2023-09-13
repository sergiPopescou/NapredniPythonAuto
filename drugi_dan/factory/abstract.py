class Person:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority

    def __str__(self):
        return f"{self.seniority} {self.name}"

class Issue:
    def __init__(self, number, difficulty, estimated=0):
        self.number = number
        self.difficulty = difficulty
        self.estimated = estimated

    def __str__(self):
        return f"Issue {self.number}"

class AbstractFactory:
    def build(self, csv):
        pass

class PersonFactory(AbstractFactory):
    def build(self, csv):
        splits = csv.split(",")
        return Person(splits[0], splits[1])

class IssueFactory(AbstractFactory):
    def build(self, csv):
        splits = csv.split(",")
        if len(splits) == 2:
            return Issue(splits[0], splits[1])
        return Issue(splits[0], splits[1], int(splits[2]))

# i nije neophodno
class Loader:
    @staticmethod
    def load(csv, factory):
        return factory.build(csv)

person = Loader.load("Mane,SENIOR", PersonFactory())
print(person)

issue = Loader.load("123,HARD,10", IssueFactory())
print(issue)


