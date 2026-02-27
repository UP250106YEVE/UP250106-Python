#30 DAYS OF PYTHON DAY 3
#OPERATORS

# - Integer, float and complex

import math

myage = 18 #Integer
myheight = 1.71 #meters, float
complex = 5+5j #Complex

# - Script for a triangle
base = float(input('Introduzca la base del triángulo: '))
height = float(input('Introduzca la altura del triángulo: '))

# - Calculate the surface area

area = ((base*height)/2)
print('El área del triángulo es: ', area)

# - Script for entering a,b,c in a triangle, calculate perimeter

sidea = float((input('Escriba el lado A del triángulo: ')))
sideb = float((input('Escriba el lado B del triángulo: ')))
sidec = float((input('Escriba el lado C del triángulo: ')))

perimeter = sidea + sideb + sidec

print('El perímetro del triángulo es: ', perimeter)

# - Length and width of a rectangle + calculate area

rsidea = float(input('Escriba el lado A del rectángulo: '))
rsideb = float(input('Escriba el lado B del rectángulo: '))

rarea = rsidea * rsideb
rperimeter = rsidea*2 + rsideb*2

print('El área del rectángulo es: ',rarea)
print('El perímetro del rectángulo es: ',rperimeter)

# - Radius of a Circle, area, circumference

radius = float(input('Introduzca el radio del círculo: '))

carea = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print('El área del círculo es: ', carea, 'aprox.')
print('La circunferencia del círculo es: ', circumference, 'aprox.')

# - Slope, x and y intercept of y=2x-2

# Equal each variable in the ecuation as '0' and solve the intercepts
# They will be such as X = 1 and Y = -2, and for the slop we should get the value aside X, which is '2'

m = 2
ecy = -2
ecx = 1

print('La pendiente es: ', m)
print('La intersección en X es: ', ecx)
print('La intersección en Y es: ', ecy)

# Find the slope and Euclidean distance between p1(2,2) & p2(6,10)

x1, y1 = 2, 2
x2, y2 = 6, 10

m2 = (y2 - y1 / x2 - x1)

dist2 = math.hypot (x2 - x1, y2 - y1)

print('La pendiente de los puntos es: ', m2)
print('La hipotenusa de los puntos es: ', dist2)

# - Compare the slops of the previous tasks

if m==m2: 
    print('Las dos pendientes son iguales')
else:
    print('Las pendientes son diferentes. ''Pendiente 1: ',m,' ''Pendiente 2: ',m2 )


# - Calculate value of (y=x^2+6x+9)

def calculate_y(x):
    return x**2 + 6*x + 9

# 1. Calculating values for a specific range
print("Calculo para valores en X:")
for x in range(-6, 2):
    y = calculate_y(x)
    print(f"x = {x}, y = {y}")

# 2. Finding the root where y = 0 using the quadratic formula
a = 1
b = 6
c = 9

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    # There is at least one real root
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    if root1 == root2:
        print(f"\nHay una única solución: x = {root1}")
    else:
        print(f"\nSoluciones donde Y es 0: x = {root1} and x = {root2}")
else:
    print("\nNo hay soluciones reales (raíces complejas).")

# - Find the length of 'python' and 'dragon' with a falsy comparison
print('Comparar el largo de las palabras:')

if(len('python')) == len('dragon'):
    print('"python" es igual de largo que "dragon"')

if(len('python')) > len('dragon'):
    print('la palabra "python" es más larga')

if(len('python')) < len('dragon'):
    print('la palabra "dragon" es más larga')

    sentence = "I hope this course is not full of jargon."
word_to_check = "jargon"

# - Jargon in sentence

sentence = "I hope this course is not full of jargon."
word_to_check = "jargon"

if word_to_check in sentence:
    print(f"Yes, '{word_to_check}' was found in the sentence.")
else:
    print(f"No, '{word_to_check}' is not there.")

# - No 'on'

words = ["dragon", "python"]
substring = "on"

for word in words:
    if substring in word:
        print(f"Actually, '{substring}' IS in '{word}'.")
else:
    print("Wait, the sentence was a trick!")

# - Length of 'python' and convert value

texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)

#Results
print(f"Texto: {texto}")
print(f"Longitud como entero: {longitud}")
print(f"Longitud como float: {longitud_float}")
print(f"Longitud como string: '{longitud_str}'")

# - Floor division of 7 by 3
resultado_division = 7 // 3

#2.7
resultado_entero = int(2.7)
son_iguales = resultado_division == resultado_entero

print(f"7 // 3 = {resultado_division}")
print(f"int(2.7) = {resultado_entero}")
print(f"¿Son iguales? {son_iguales}")

# - 10 equal type 10

tipo_texto = type('10')
tipo_entero = type(10)
son_tipos_iguales = tipo_texto == tipo_entero

print(f"Tipo de '10': {tipo_texto}")
print(f"Tipo de 10: {tipo_entero}")
print(f"¿Son los tipos iguales? {son_tipos_iguales}")

# - Check 9.8 int == 10 and divisible by 2

numero=int(input("\nIngresa un numero para saber si es par o impar: "))
print("Tu número es ",("Par" if numero % 2 == 0 else "Impar"))
print (type(10)==type(10))
print(int(9.8)==10)

# - Calculate the salary

print("\nCalcular el salario de una persona")
hora=float(input("Cuantas horas trabajo: "))
salperhora=float(input("Cuanto es su salario por hora: "))
salario=hora*salperhora
print("El salario final es de: ",salario)

# - Years lived

añosvida=int(input("\nIngresa el número de años que has vivido:"))
segundos=añosvida*365*24*60*60
print("Tu has vivido por ",segundos," segundos")

# - Following table

print("\nLa tabla es: ")

for i in range(1, 6):  # From 1 to 5

    print(i, 1, i, i*2, i*3)