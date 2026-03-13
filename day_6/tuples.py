#Day_6
#Excercises level 1
empty_tuple = ()
print('Empty tuple: ', empty_tuple)
sisters_names = ('Fabiola', 'Cristina', 'Nancy')
print('Sisters names: ', sisters_names)
brothers_names = ('Yexuanj', 'Armando', 'Juan Carlos')
print('Brothers names: ', brothers_names)
siblings_names = sisters_names + brothers_names
print('Siblings names: ', siblings_names)
print('I have', len(siblings_names), 'siblings')
family_members = list(siblings_names)
family_members.append('Ricardo')
family_members.append('Rodolfo')
print('Family members: ', family_members)
family_members = tuple(family_members)