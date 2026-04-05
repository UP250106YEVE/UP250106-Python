#Day_11
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
