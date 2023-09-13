from .kancelarija import Office
class Address:
    def __init__(self, street_address, office, city):
        self.street_address = street_address
        self.office = office
        self.city = city

    def __str__(self):
        return f'{self.street_address}, {self.office}, {self.city}'

