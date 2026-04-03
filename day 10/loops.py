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