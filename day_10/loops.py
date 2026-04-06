#Day_10
print('EXCERCISES LEVEL 1')
print('EXCERCISE 1')
print('For loop: ')
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
for number in numbers:
    print(number)

print('While loop: ')
count = 0
while count <= 10:
    print(count)
    count += 1
print('EXCERCISE 2')
print('Backwards using For loop: ')
for number in reversed(numbers):
    print(number)

print('Backwards using While loop: ')
count = 10
while count >= 0:
    print(count)
    count -= 1
print('EXCERCISE 3')
line = '#'
while len(line) <= 7:
    print(line)
    line += '#'
print('EXCERCISE 4')
for row in range(8):
    for col in range (8):
        print('#', end = ' ')
    print()
print('EXCERCISE 5')
for i in range(11):
    result = i * i
    print(f'{i} * {i} = {result}')
print('EXCERCISE 6')
items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in items:
    print(item, end=', ')
print(' ')
print('EXCERCISE 7')
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=', ')
print(' ')
print('EXCERCISE 8')
for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=', ')
print(' ')
print(' ')
print('EXCERCISES LEVEL 2')
print('EXCERCISE 1')
total = 0
for number in range(1,101):
    total += number
print('The sum of all numbers from 1 to 100 is: ', total)
print(' ')
print('EXCERCISE 2')
sum_even = 0
sum_odd = 0
for number in range(0,101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
print(f'The sum of even numbers in the range 0 to 100 is {sum_even} and the sum of odd numbers is {sum_odd}')
print(' ')
print('EXCERCISES LEVEL 3')
print('EXCERCISE 1')
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