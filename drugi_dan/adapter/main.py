from drugi_dan.adapter.adapter import Adapter
from animal_kingdom import Animal

if __name__ == "__main__":
    animal = Animal("ime", 3, "Protozoe")
    for ispis in Adapter(animal):
        ispis.ispis()
