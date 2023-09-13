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

    @staticmethod
    def new_csv_animal(csv_string):
        splits = csv_string.split(",")
        return Animal(splits[0], int(splits[1]), splits[2])


animal = Animal.new_csv_animal("Chilly,2,Penguin")
print(animal)