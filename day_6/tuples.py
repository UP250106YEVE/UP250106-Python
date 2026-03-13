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
family_members.append('Juan Andres')
family_members.append('Sara Eudave')
print('Family members: ', family_members)
family_members = tuple(family_members)
#Excercises level 2
print(' ')
print('Unpacking siblings, father and mother')
*sibs, father, mother = family_members
print('Siblings: ', sibs)   
print('Father: ', father) 
print('Mother: ', mother)

fruits = ('Apple', 'Banana', 'Orange', 'Grape')
print('Fruits: ', fruits)
vegetables = ('Carrot', 'Cilantro', 'Onion')
print('Vegetables: ', vegetables)
animal_products = ('Food', 'Soap', 'Leather')
print('Animal products: ', animal_products)
food_stuff_tp = fruits + vegetables + animal_products
animal_products = ('Food', 'Soap', 'Leather')
print('Animal products: ', animal_products)
food_stuff_tp = fruits + vegetables + animal_products
print('All together: ', food_stuff_tp)
food_stuff_tp_list = list(food_stuff_tp)
print('Tuple to list: ', food_stuff_tp_list)
carrot_and_cilantro = food_stuff_tp[4:6]
print('Slicing out the middle items: ', carrot_and_cilantro)
apple_banana_orange = food_stuff_tp[0:3]
print('Slicing out the first three items: ', apple_banana_orange)
foos_soap_leather = food_stuff_tp[-3:]
print('Slicing out the last three items: ', foos_soap_leather)
del food_stuff_tp
print(' ')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Nordic countries: ', nordic_countries)
print('Is Estonia in Nordic countries? ', 'Estonia' in nordic_countries)
print('Is Iceland in Nordic countries?', 'Iceland' in nordic_countries)