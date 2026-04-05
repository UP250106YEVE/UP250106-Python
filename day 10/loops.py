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

from countries import countries
countries_with_land = []
for country in countries:
    if 'land' in country.lower():
        countries_with_land.append(country)
print('Countries with \'land\' in countries.py file: ', countries_with_land)
print(' ')
print('EXCERCISE 2')
fruit_list =  ['banana', 'orange', 'mango', 'lemon']
reversed_fruit_list = []
for i in range(len(fruit_list) -1, -1, -1):
    reversed_fruit_list.append(fruit_list[i])
print('Original list: ', fruit_list)
print('Reversed list: ', reversed_fruit_list)
print(' ')
print('EXCERCISE 3')
from countries_data import countries
all_languages = []
for country in countries:
    all_languages.extend(country['languages'])
unique_languages = set(all_languages)
print(f'Total number of unique languages: {len(unique_languages)}')

from collections import Counter
language_counts = Counter(all_languages)
most_spoken = language_counts.most_common(10)
print('Ten monst spoken languages: ', most_spoken)
print(' ')
print('Most populated countries')
sorted_countries = sorted(countries, key = lambda x: x['population'], reverse=True)
top_10_populated = sorted_countries[:10]
for country in top_10_populated:
    print(f'{country['name']}: {country['population']}')