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

