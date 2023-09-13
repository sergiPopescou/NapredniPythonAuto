
class Office:
    def __init__(self, floor, number):
        self.number = number
        self.floor = floor

    def __str__(self):
        return f'Floor {self.floor}, Number {self.number}'
