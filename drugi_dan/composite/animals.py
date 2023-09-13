class Kompozicija:
    def __init__(self, name):
        self.children = []
        self.name = name

    def __str__(self):
        return f"{self.name} {','.join([str(i) for i in self.children])}"

class Animal():
    def __init__(self, name):
        self.name = name
        self._species_ = "UNKNOWN"

    # if changed, it is a polymorphism
    def say(self, something):
        print("%s %s says %s" % (self._species_, self.name, something))

    # if not changed, it is a reusability a.k.a DRY concept
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Animal[%s]" % self._species_

    # encapsulation
    def setSpecies(self, species):
        self._species_ = species

    def getSpecies(self):
        return self._species_


class Dog(Animal):  # inheritance
    def __init__(self, name, race):
        super().__init__(name)  # DRY concept
        self.race = race
        self.setSpecies("Dog")

class Horse(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self._species_ = "Horse"



class Robot:
    def __init__(self, type_, serialNumber):
        self.type_ = type_
        self.SN = serialNumber

    def __str__(self):
        return "Robot %s with S/N: %s" % (self.type_, self.SN)
    def __repr__(self):
        return "Robot %s with S/N: %s" % (self.type_, self.SN)
    def walk(self):
        print("Robot %s with S/N: %s IS WALKING" % (self.type_, self.SN))

    def say(self, robot_says):
        print("Robot %s with S/N: %s says: %s" % (self.type_, self.SN, robot_says))




class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._species_ = "Bird"

    def flap(self):
        print("%s flaps!" % self)

    def fly(self):
        self.flap()
        self.flap()
        self.flap()
        self._fly_()

    def _fly_(self):
        print("%s flies!" % self)


class Penguin(Bird):  # mulitiple inheritance, multilevel inheritance
    def __init__(self, name):
        super().__init__(name)
        self._species_ = "Penguin"

    def _fly_(self):  # method overwriting
        print("%s flies NOT!" % self)

    def eat(self):
        print("%s eats FISH" % self);





class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._species_ = "Elephant"

    def eat(self):
        print("%s eats tons of peanut!" % self);




class WTFIsThis(Penguin, Elephant):  # multiple inheritance
    def __init__(self, name):
        super().__init__(name)
        self._species_ = self.__class__.__name__


elephant = Elephant("Ellie")
wtf = WTFIsThis("ChillyEllie")
penguin = Penguin("Chilly Willie")
robot = Robot("HODAJUCI", 123456)
horse = Horse("Cetalj", "ridjan")
dog = Dog("pas", "avlijaner")

zoo = Kompozicija("Zooloski")
zoo.children.append(robot)
ostale = Kompozicija("Zivotinje")
ostale.children.append(dog)
ostale.children.append(horse)
ostale.children.append(penguin)
ostale.children.append(wtf)
ostale.children.append(elephant)
zoo.children.append(ostale)
print(str(zoo))


