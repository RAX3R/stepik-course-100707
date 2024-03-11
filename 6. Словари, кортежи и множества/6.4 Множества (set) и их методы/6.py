city = input()

cities = set()

while city != "q":
    cities.add(city)
    city = input()

print(len(cities))
