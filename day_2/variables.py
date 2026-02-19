#Day 2: 30 DAYS OF PYTHON

#EXERCISES L1
first_name = 'Yexuanj Ernesto'
last_name = 'Velasco Eudave'
full_name = 'Yexuanj Ernesto Velasco Eudave'
country = 'México'
city = 'Aguascalientes'
age = 18
year = 2026
is_married = False
is_true = True
its_light_on = True
year_of_birth, career = 2007, 'Ing. Mecatrónica'

#EXERCISES L2 
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(its_light_on))
print(type(year_of_birth))

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))

# NUMERIC VARIABLES
num_one = 5   # ASIGN TO num_one
num_two = 4   # ASIGN TO num_two

# BASIC MATH
total = num_one + num_two          # SUM num_one & num_two
diff = num_one - num_two           # SUB num_two FROM num_one
product = num_one * num_two        # MULT OF num_one & num_two
division = num_one / num_two       # DIV OF num_one & num_two
remainder = num_two % num_one      # MODULE: RESIDUE num_two & num_one
exp = num_one ** num_two           # POW: num_one  TO num_two
floor_division = num_one // num_two # FLOOR DIVISION

# CRICLE CALCULUS
radius = 30   # RADIUS IN METERS
pi = 3.14159  # APROXIMATE π VALUE

area_of_circle = pi * radius ** 2       # CIRCLE SURFACE: π * r^2
circum_of_circle = 2 * pi * radius      # CIRCUMFERENCE: 2 * π * r

# SHOW RESULTS
print("Suma:", total)
print("Resta:", diff)
print("Multiplicación:", product)
print("División:", division)
print("Residuo:", remainder)
print("Potencia:", exp)
print("División entera:", floor_division)
print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# TAKING RADIUS
radius_input = float(input("Introduce el radio del círculo: "))
area_input = pi * radius_input ** 2
print("Área del círculo con radio ingresado:", area_input)

# COLLECT DATA
first_name = input("Introduce tu nombre: ")
last_name = input("Introduce tu apellido: ")
country = input("Introduce tu país: ")
age = input("Introduce tu edad: ")

print("Nombre:", first_name)
print("Apellido:", last_name)
print("País:", country)
print("Edad:", age)

# SHOW RES. WORDS IN PYTHON
help('keywords')