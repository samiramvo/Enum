from enum import Enum, IntEnum
class Country(IntEnum):
    Afghanistan=93
    Albania=355
    Algeria=313

print('Trier les villes par ordre')
print('\n'.join(' '+c.name for c in sorted(Country)))