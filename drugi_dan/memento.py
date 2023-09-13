
class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f'Balance = {self.balance}'


if __name__ == '__main__':
    BA = BankAccount(100)
    M1 = BA.deposit(50)
    M2 = BA.deposit(25)
    print(BA)

    # restore to M1
    BA.restore(M1)
    print(BA)

    # restore to M2
    BA.restore(M2)
    print(BA)