#Day 2: 30 DAYS OF PYTHON

#Exercises Level 1
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

#Exercises Level 2
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

# Declaramos las variables numéricas
num_one = 5   # Asignamos el valor 5 a la variable num_one
num_two = 4   # Asignamos el valor 4 a la variable num_two

# Operaciones básicas
total = num_one + num_two          # Suma de num_one y num_two
diff = num_one - num_two           # Resta de num_two a num_one
product = num_one * num_two        # Multiplicación de num_one y num_two
division = num_one / num_two       # División de num_one entre num_two
remainder = num_two % num_one      # Módulo: residuo de dividir num_two entre num_one
exp = num_one ** num_two           # Potencia: num_one elevado a num_two
floor_division = num_one // num_two # División entera (floor division)

# Cálculos con círculo
radius = 30   # Radio del círculo en metros
pi = 3.14159  # Valor aproximado de π

area_of_circle = pi * radius ** 2       # Área de un círculo: π * r^2
circum_of_circle = 2 * pi * radius      # Circunferencia: 2 * π * r

# Mostrar resultados
print("Suma:", total)
print("Resta:", diff)
print("Multiplicación:", product)
print("División:", division)
print("Residuo:", remainder)
print("Potencia:", exp)
print("División entera:", floor_division)
print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# Tomar radio como entrada del usuario
radius_input = float(input("Introduce el radio del círculo: "))
area_input = pi * radius_input ** 2
print("Área del círculo con radio ingresado:", area_input)

# Solicitar datos personales al usuario
first_name = input("Introduce tu nombre: ")
last_name = input("Introduce tu apellido: ")
country = input("Introduce tu país: ")
age = input("Introduce tu edad: ")

print("Nombre:", first_name)
print("Apellido:", last_name)
print("País:", country)
print("Edad:", age)

# Ver palabras reservadas en Python
help('keywords')