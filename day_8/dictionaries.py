#EXERCISES
dog = {}

dog = {'name':'Mandarino',
    'color':'Yellow',
    'breed':'si',
    'legs':'orange',
    'age':'at least 1 day'}
print(dog)

student = {'first_name':'Yex',
        'last_name':'vela',
        'gender':'Male',
        'age':'18',
        'marital_status':'Con mi mujer',
        'skills':['habilidad1','habilidad2'],
        'country':'Mexico',
        'City':'Aguascalientes',
        'adress':'Fco. I. Madero. #238, Calvillo'
        }
print(student)

print(len(student))

student['skills'].append('habilidad3')
print(student)

keys = student.keys()
print(keys)

values = student.values()
print(values)

print(student.items())

del student['skills']
print(student)

del student