cuenta = 0
while cuenta < 11:
    print(cuenta)
    cuenta += 1

cuenta2 = 10
while cuenta2 >= 0:
    print(cuenta2)
    cuenta2 -= 1

signo = "#"
while len(signo) <= 7:
    print(signo)
    signo += "#"

for fila in range(8):
    for columna in range(8):
        print("#", end=" ")
    print()

for i in range(11):
    print(f"{i} x {i} = {i * i}")

librerias = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in librerias:
    print(item)

for i in range(0, 101, 2):
    print(i)

for i in range(1, 101, 2):
    print(i)
