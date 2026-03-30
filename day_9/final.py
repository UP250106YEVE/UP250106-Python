a = float(input("Ingrese el primer número A: "))
b = float(input("Ingrese el segundo número B: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{b} es mayor que {a}")
else:
    print(f"{a} y {b} son iguales")