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


age_a = int(input('Introduce tu edad: '))
age_b = int(input('Introduce la edad de tu amigo: '))

if age_a > age_b:
    print('Eres mayor que tu amigo')
elif age_a < age_b:
    print('Tu amigo es mayor que tú')
else:
    print('Tienen la misma edad')



califacion = float(input('Introduce tu calificación: '))

if califacion >= 90:
    print('¡Excelente! Obtuviste una A')

if califacion >= 80 and califacion < 90:
        print('¡Muy bien! Obtuviste una B')

if califacion >= 70 and califacion < 80:
            print('¡Bien! Obtuviste una C')
if califacion >= 60 and califacion < 70:
                print('¡Suficiente! Obtuviste una D')
if califacion < 60:
                    print('¡Insuficiente! Obtuviste una F')


mes = (input('Introduce el mes del año: '))

if mes == 'diciembre' or mes == 'enero' or mes == 'febrero':
    print('Estamos en invierno')

elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
        print('Estamos en primavera')

elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
            print('Estamos en verano')

elif mes == 'septiembre' or mes == 'octubre' or mes == 'noviembre':
                print('Estamos en otoño')


fruits = ['banana', 'orange', 'mango', 'lemon']

print('Frutas disponibles:', fruits)
fruit = input('Introduce el nombre de una fruta: ')

if fruit in fruits:
    print('La fruta', fruit, 'ya existe en la lista')

if fruit not in fruits:
    print('La fruta', fruit, 'no existe está en la lista')
    print('Deseas agregar', fruit, 'a la lista? (Si/No)')
if input().lower() == 'si':
    fruits.append(fruit)
    print('Fruta agregada. Lista actualizada:', fruits)
else:    print('Fruta no agregada. Lista actual:', fruits)


person={
    'first_name': 'Yexuanj',
    'last_name': 'Velasco',
    'age': 18,
    'country': 'Mexico',
    'is_married': True,
    'skills': ['Python'],
    'address': {
        'street': 'Calvillo',
        'zipcode': '20834'
    }
    }
print(person)
if 'skills' in person:
        skills = person['skills']
        middle_index = len(skills) // 2
        print('La habilidad del medio es:', skills[middle_index])
if 'Python' in person['skills']:
    print('¡Tienes habilidades en Python!')
else:
    print('No tienes habilidades en Python')

if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('Eres un desarrollador front-end')
elif'Node' in person['skills'] and 'Python' in person['skills'] and 'Node' in person['skills']:
    print('Eres un desarrollador back end')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'Mongo' in person['skills']:
    print('Eres un desarrollador full stack')
else :    print('Eres un desarrollador desconocido')

if person['is_married'] and person['country'] == 'Mexico':
    print(person['first_name'], person['last_name'], 'es un mexicano casado')