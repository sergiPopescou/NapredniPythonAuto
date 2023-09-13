from drugi_dan.bridge.persisters import *
class Animal:
    def __init__(self, name, persister, legs=0, species="UNKNOWN"):
        self.name = name
        self.persister = persister
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

    def persist(self):
        self.persister.persist(self)


if __name__ == "__main__":
    ppersister = PrintPersister()
    an = Animal("protozoe", ppersister)
    an.persist()

