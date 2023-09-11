class Dog():
    velicina_copora = 0
    def __init__(self, name):
        self.name = name
        self.legs = 4
        Dog.velicina_copora += 1

    @classmethod
    def print_copor(cls):
        print(cls.velicina_copora)
    def say(self):
        print("bark")

    @staticmethod
    def veterinar(pas):
        print("operacija")
        pas.say()
        pas.legs = 3

class Robot:
    def __init__(self, sn):
        self.serial = sn

    def say(self):
        print(f"robot kaze {self.serial}")


pas = Dog("Pujdo")
pas.say()
Dog.print_copor()
print(pas.__dict__)
print(pas.__class__.__dict__)
robot = Robot("123")
lista = [pas, robot]
for i in lista:
    i.say()