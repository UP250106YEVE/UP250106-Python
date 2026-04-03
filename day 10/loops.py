cuenta = 0
while cuenta < 11:
    print(cuenta)
    cuenta += 1

cuenta2 = 10
while cuenta2 >= 0:
    print(cuenta2)
    cuenta2 -= 1

signo = "#"
while len(signo) <= 7:
    print(signo)
    signo += "#"

for fila in range(8):
    for columna in range(8):
        print("#", end=" ")
    print()

for i in range(11):
    print(f"{i} x {i} = {i * i}")

librerias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in librerias:
    print(item)

for i in range(0, 101, 2):
    print(i)

for i in range(1, 101, 2):
    print(i)

countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_with_land = []

for country in countries:
    if 'land' in country.lower():
        countries_with_land.append(country)

print(countries_with_land)


fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)

languages_set = set()

for country in countries:
    for lang in country['languages']:
        languages_set.add(lang)

print(f"Total de idiomas: {len(languages_set)}")


most_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Top 10 países más poblados:")
for i in range(10):
    country = most_populated[i]
    print(f"{i+1}. {country['name']}: {country['population']}")