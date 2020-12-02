from pint import UnitRegistry
unitregistry = UnitRegistry()

def convert(msrmt, unit, new_unit):
    return (msrmt * getattr(unitregistry, unit)).to(getattr(unitregistry, new_unit))

print("msrmt: 6")
print("unit: cup")
print("new_unit: gallon")

conversion = convert(6, "cup", "gallon")
print(conversion)


