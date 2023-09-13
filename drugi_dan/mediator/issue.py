class Issue:
    def __init__(self, number):
        self.number = number
        self.people = []

    def broadcastReview(self, reviewer, review):
        for p in self.people:
            if p.name != reviewer:
                p.setReview(reviewer, review)

    def join(self, person):
        print(f'{person.name} joins the issue')
        person.joinTheIssue(self)
        self.people.append(person)
