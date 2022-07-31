from enum import Enum
class Country(Enum):
    Albania=355
    Andorra=376
    Angola=244

print("Member name:{}".format(Country.Albania.name))
print("Member name:{}".format(Country.Albania.value))

