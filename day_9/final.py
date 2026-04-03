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