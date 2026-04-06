print('EXCERCISES LEVEL 1')
def add_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', add_two_numbers(2, 3))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print('Area of circle: ', area_of_circle(4))

def add_all_nums (*nums):
    total = 0
    for num in nums:
        total += num
    return total
print('Adding nums 5, 4 and 6: ', add_all_nums(5, 4, 6))

def convert_celsius_to_fahrenheit (C):
    F = (C * 9/5) +32
    return F
print('Celsius to fahrenheit: ', convert_celsius_to_fahrenheit(30), '°F')

def check_season (month):
    if month in ['September', 'October', 'November']:
        season = str('Autumn')
    elif month in ['December', 'January', 'February']:
        season = str('Winter')
    elif month in ['March', 'April', 'May']:
        season = str('Spring')
    elif month in ['June', 'July', 'August']:
        season = str('Summer')
    else:
        season = str('There is no season for this month')
    return season
print('Check season: ', check_season('November'))

def calculate_slope (x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'Slope is undefined (vertical line)'
    slope = (y2 - y1)/(x2-x1)
    return slope
print('Calculate slope: ', calculate_slope(1, 2, 3, 4))

def solve_quadratic_eqn (a, b, c):
    discriminant = b**2 - 4*a*c
    if a == 0:
        return "Not a quadratic equation (a cannot be 0)"
    import math
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return {x1, x2}
    elif discriminant == 0:
        x = -b / (2*a)
        return {x}
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return {root1, root2}
print('Solve quadratic equation: ', solve_quadratic_eqn(1, -5, 6))

def print_list (my_list):
    for element in my_list:
        print('List element: ', element)
car_brands = ['Volkswagen', 'Porsche', 'Audi', 'BMW']
print_list(car_brands)

def reverse_list (array):
    reverse_array = []
    for i in range(len(array)-1, -1, -1):
        reverse_array.append(array[i])
    return reverse_array
print('Reversed list: ', reverse_list([1, 2, 3, 4, 5]))
print('Reversed list: ', reverse_list(['A', 'B', 'C']))

def capitalize_list_items(my_list):
    capitalized_list = []
    for item in my_list:
        capitalized_list.append(str(item).capitalize())
    return capitalized_list
objects = ['paper', 'wallet' , 'bottle', 'backpack']
print('Capitalized llist: ', capitalize_list_items(objects))

def add_item(my_list, item):
    new_list = my_list.copy()
    new_list.append(item)
    return new_list
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print('Adding item to list: ', add_item(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9]
print('Adding item to list: ', add_item(numbers, 5))

def remove_item (my_list, item):
    new_list = my_list.copy()
    new_list.remove(item)
    return new_list
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print('Removing item: ', remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print('Removing item: ', remove_item(numbers, 3))

def sum_of_numbers (n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print('Sum of numbers in range 0-5: ', sum_of_numbers(5))
print('Sum of numbers in range 0-10: ', sum_of_numbers(10))
print('Sum of numbers in range 0-100: ', sum_of_numbers(100))

def sum_of_odds (n):
    total = 0
    for i in range (n + 1):
        if i % 2 != 0:
            total += i
    return total
print('Sum of odds in range 0-10: ', sum_of_odds(10))

def sum_of_evens (n):
    total = 0
    for i in range (n + 1):
        if i % 2 == 0:
            total += i
    return total
print('Sum of evens in range 0-10: ', sum_of_evens(10))
print(' ')
print('EXCERCISES LEVEL 2')
def evens_and_odds (n):
    evens = 0
    odds = 0
    for i in range (n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f'The number of odds in range 0-100 is: {odds}')
    print(f'The number of evens in range 0-100 is: {evens}')
evens_and_odds(100)

def factorial (n):
    if n < 0:
        return 'Error: Negative numbers dont have factorials'
    result = 1
    for i in range(1, n + 1 ):
        result *= i
    return result
print('Factorial of 5: ', factorial(5))

def is_empty (parameter):
    if len(parameter) == 0:
        return True
    else:
        return False
print('Is empty?', is_empty([]))
print('Is empty?', is_empty(['Hello']))
print('Is empty?', is_empty({}))

import math
def calculate_mean (data):
    return sum(data) / len(data)
def calculate_median (data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]
def calculate_mode (data):
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1

    max_count = max(counts.values())
    modes = [key for key, val in counts.items() if val == max_count]
    return modes
def calculate_range (data):
    return max(data) - min(data)
def calculate_variance (data):
    mu = calculate_mean(data)
    return sum((x - mu) ** 2 for x in data) / len(data)
def calculate_std (data):
    variance = calculate_variance(data)
    return math.sqrt(variance)
test_scores = [85, 90, 78, 90, 92]
print('Test scores: ', test_scores)
print(f"Mean: {calculate_mean(test_scores)}")
print(f"Median: {calculate_median(test_scores)}")
print(f"Mode: {calculate_mode(test_scores)}")
print(f"Range: {calculate_range(test_scores)}")
print(f"Std Dev: {calculate_std(test_scores):.2f}")

def greet (name = 'Guest'):
    print(f'Hello, {name}!')
greet()
greet('Santos')

def show_args (**kargs):
    output_parts = []
    for name, value in kargs.items():
        output_parts.append(f"{name}: {value}")
    print("Received: " + ", ".join(output_parts))
show_args(name = 'Alice', age = 30, city = 'New York')
show_args(name = 'Bob', pet = 'Fluffy, the bunny')
print(' ')
print('EXCERCISES LEVEL 3')
