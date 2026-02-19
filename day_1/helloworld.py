# Day 1 if 30-days of python

# DAY 1 LEVEL 1

# OPERATORS

print (3+1)
print (3-5)
print (3/2)
print (3*1)
print (3**2)
print (3%1)
print (3//1)

# STRINGS

print(type('Yexuanj Ernesto'))
print(type('Velasco Eudave'))
print(type('Mexico'))
print(type('I am enjoying 30 days of python'))

# DATA TYPES

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Yexuanj Ernesto', 'Python', 'Mexico']))
print(type('Yexuanj Ernesto'))
print(type('Velasco Eudave'))
print(type('Mexico'))

# EXERCISE 4, CHECKING DATA TYPES

print(type(15)) #INT
print(type(1.618)) #FLOAT
print(type(5+5j)) #COMPLEX

print(type('Calvillo')) #STRING

yxj = True
print(type(yxj)) #BOOLEAN
print(type(['Santos','Jime','Yex','Efra'])) #LIST
print(type({82, 390, 1, 4})) #SET
print(type({'Yex':'Vela'})) #DICTIONARY
print(type(('HOLA','HELLO','BONJOUR'))) #TUPLE

#COORDENADAS 'M'

import math

x1, y1 = 2, 3
x2, y2 = 10, 8

#EUCLIDEAN DISTANCE

dist = math.sqrt ((x2 - x1)*2 + (y2 - y1)*2)

print('Euclidean Distance is:', dist)