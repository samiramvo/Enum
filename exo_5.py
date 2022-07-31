import enum 
class Country(enum.Enum):
    Afghanistan=93
    Albania=355
    Algeria=313
for a in Country:
    print('{}={}'.format(a.name,a.value))
