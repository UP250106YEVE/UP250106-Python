edad = int(input('Introduce tu edad:'))

if edad < 18:
    print('Aún no tienes edad para conducir')
    faltan = 18 - edad
    print('Faltan', faltan, 'años para que puedas conducir')
else:
    print('¡Felicidades! Ya puedes conducir')

a = float(input("Ingrese el primer número A: "))
b = float(input("Ingrese el segundo número B: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{b} es mayor que {a}")
else:
    print(f"{a} y {b} son iguales")