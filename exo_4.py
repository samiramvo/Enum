from enum import IntEnum
class Country(IntEnum):
    Afghanistan=93
    Albania=355
    Algeria=313

country_list=list(map(int,Country))
print(country_list)