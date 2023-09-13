class Issue:
    def __init__(self, number, dif):
        self.number = number
        self.difficulty = dif

    def __str__(self):
        return f'Issue {self.number}, difficulty {self.difficulty}'
