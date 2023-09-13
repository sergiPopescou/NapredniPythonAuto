import copy
from drugi_dan.prototype.osoba import Employee
from drugi_dan.prototype.adresa import Address
from drugi_dan.prototype.kancelarija import Office


class EmployeeFactory:
    tttech_employee = Employee('', Address('Vuka Karadzica 6', None, 'Banjaluka'))
    rtrk_employee = Employee('', Address('Jovana Ducica 23', None, 'Banjaluka'))

    @staticmethod
    def __new_employee(proto, name, office):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.office = office
        return result

    @staticmethod
    def new_tttech_employee(name, office):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.tttech_employee,
            name, office
        )

    @staticmethod
    def new_rtrk_employee(name, office):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.rtrk_employee,
            name, office
        )


aleksa = EmployeeFactory.new_tttech_employee('Aleksa Avramovic', Office(3, "Zavicaj"))
ognjen = EmployeeFactory.new_rtrk_employee('Ognjen Stojcic', Office(3, 11))

print(aleksa)
print(ognjen)
