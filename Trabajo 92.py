def liters_100km_to_miles_gallon(liters_100km):

    km_per_mile = 1/1.609344
    liters_per_gallon = 3.785411784
    return 100 / (liters_100km / km_per_mile / liters_per_gallon)

def miles_gallon_to_liters_100km(miles_gallon):
    km_per_ile = 1 / 1.609344
    liters_per_gallon = 3.785411784
    return 100 / (miles_gallon * km_per_mile / liters_per_gallon)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(liters_100km_to_miles_gallon(60.3))

