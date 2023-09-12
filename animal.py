class Animal:
    def __init__(self, name, legs=0, species="UNKNOWN"):
        self.name = name
        self._legs_ = legs
        self._species_ = species

    # if changed, it is a polymorphism
    def say(self, something=None):
        print("%s %s says %s" % (self._species_, self.name, something))

    # def eat(self):
    #     print(f"{self.species} is eating")

    def eat(self, something=""):
        print(f"{self.species} is eating {something}")

    def move(self):
        pass
    # if not changed, it is a reusability a.k.a DRY concept

    def __str__(self):
        return str(self.__dict__)
        # return self.__repr__()

    def __repr__(self):
        return "Animal[%s], name=%s" % (self._species_, self.name)

    # encapsulation
    @property
    def legs(self):
        return self._legs_

    @legs.setter
    def legs(self, value):
        self._legs_ = value

    @property
    def species(self):
        return self._species_


an = Animal("protozoe")
print(an)
an.say("blah")
an.eat("nothing")
an.move()
print(Animal.mro())


animal = Animal("ime")
print("Ime zivotinje je %s" % animal.name)


class Dog(Animal):  # inheritance
    def __init__(self, name, race):
        super().__init__(name, 4, "Dog")  # DRY concept
        self.race = race


dog = Dog("pas", "avlijaner")
dog.say("nesto")
print("Ime zivotinje je %s" % dog.name)


class Horse(Animal):
    def __init__(self, name, color):
        super().__init__(name, 4, "Horse")
        self.color = color


horse = Horse("Cetalj", "ridjan")
horse.say("njihaaa")


class Robot:
    def __init__(self, type_, serialNumber):
        self.type_ = type_
        self.SN = serialNumber

    def move(self):
        print("Robot %s with S/N: %s IS WALKING" % (self.type_, self.SN))

    def say(self, robot_says):
        print("Robot %s with S/N: %s says: %s" % (self.type_, self.SN, robot_says))


robot = Robot("HODAJUCI", 123456)
robot.move()


class Bird(Animal):
    def __init__(self, name, species="Bird"):
        super().__init__(name)

    def move(self):
        self.fly()
    def flap(self):
        print("%s flaps!" % self)

    def fly(self):
        self.flap()
        self.flap()
        self.flap()
        self._fly_()

    def _fly_(self):
        print("%s flies!" % self)

class Crow(Bird):
    def __init__(self, name):
        super().__init__(name, "Crow")


bird = Crow("Wilie")


class Penguin(Bird):  # mulitiple inheritance, multilevel inheritance
    def __init__(self, name):
        super().__init__(name, species="Penguin")

    def _fly_(self):  # method overwriting
        print("%s flies NOT!" % self)

    def eat(self):
        print("%s eats FISH" % self)


penguin = Penguin("Chilly Willie")

# polymorphism
animals = [dog, horse, robot, bird, penguin]
for animal in animals:
    animal.say("isto")
    print(animal)

print(Penguin.mro())  # Method Resolution Order

birds = [bird, penguin]
for _bird in birds:
    _bird.fly()  # which _fly_ method will be called?


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, )

    def eat(self):
        print("%s eats tons of peanut!" % self);


elephant = Elephant("Ellie")


class WTFIsThis(Elephant, Penguin):  # multiple inheritance
    def __init__(self, name):
        super().__init__(name)


if __name__ == "__main__":
    # problem sa inicijalizacijom WTF
    wtf = WTFIsThis("ChillyEllie")
    print(wtf)
    print(WTFIsThis.mro())
    wtf.eat()
    wtf.fly()

