class TehnickaOsoba:
    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.issues = []

    def joinTheIssue(self, issue):
        self.issues.append(issue)

    def setReview(self, sender, review):
        s = f'{sender}: {review}'
        print(f'[{self.name}] got review [{s}]')
        self.reviews.append(review)

    def postReview(self, issue, review):
        if issue in self.issues:
            issue.broadcastReview(self.name, review)


