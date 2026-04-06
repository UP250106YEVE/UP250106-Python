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
