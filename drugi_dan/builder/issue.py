class Issue:
    def __init__(self, project):
        self.project = project
        self.description = None
        self.person = None
        self.number = None
        self.status = "new"
        # other: numbered, assigned, open, in work, closed
        self.reviews = []

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def new():
        return IssueBuilder()


class IssueBuilder:
    def __init__(self):
        self.issue = Issue(None)

    def build(self):
        return self.issue

class IssueProjectBuilder(IssueBuilder):
    def onProject(self, project):
        self.issue.project = project
        return self

class IssueDescriptionBuilder(IssueProjectBuilder):
    def describe(self, description):
        self.issue.description = description
        return self

class IssueAssignBuilder(IssueDescriptionBuilder):
    def assign(self, person):
        self.issue.person = person
        return self

class IssueNumberingBuilder(IssueAssignBuilder):
    def identify(self, number):
        self.issue.number = number
        return self

class IssueStatusBuilder(IssueNumberingBuilder):
    def stating(self, status):
        self.issue.status = status
        return self

builder = IssueStatusBuilder()
issue = builder\
    .onProject('Projekat')\
    .describe('nesto ne radi')\
    .assign('Pero Peric')\
    .identify(333)\
    .stating('open')\
    .build()

print(issue)