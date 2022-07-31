from enum import Enum

class Country(Enum):
    Afghanitan=93
    Albania=355
    Algeria=213

for data in Country:
    print("{}={}".format(data.name,data.value))