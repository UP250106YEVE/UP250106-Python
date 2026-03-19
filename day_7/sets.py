#day_7
#EXERCISES 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Nvidia', 'Meta', 'Tesla'])
print(it_companies)

it_companies.remove('Facebook')
print(it_companies)

print('remove can, in fact, remove an element from the list or set, but it will show down an error if the element you want to remove does not exist. Either way with discard you can remove an element if it is present on the list or not without errors.')

#Excercises level 2
print('EXCERCISES LEVEL 2')
print(' ')
print('Joining A and B: ', A | B)
print('Finding intersection between A and B: ', A.intersection(B))
print('Is A subset of B? ', A.issubset(B))
print('Is A and B disjoint sets? ', A.isdisjoint(B))
print('Joining A with B', A | B)
print('Joining B with A', B | A)
print('Symmetric difference between A and B', A.symmetric_difference(B))
print('Deleting A and B sets...')
del A
del B

#Excercises level 3
print(' ')
print('EXCERCISES LEVEL 3')
print('Age in list: ', age)
age_set = set(age)
print('Age in set', age_set)
print('Lenght of \'age\' in list: ', len(age))
print('Lenght of \'age\' in set: ', len(age_set))
if len(age) > len(age_set):
    print('\'Age\' in list is larger')
else:
    print('\'Age\' in set is larger')

print(' ')
print('DIFFERENCE BETWEEN STRING, LIST, AND TUPLE')
string = 'Text'
list = [1, 2, 3]
tuple = (1, 2, 3)
print('String: ', string, '\'Immutable (cannot change after creation)\'')
print('List: ', list, '\'Mutable (can add, remove, or change items)\'')
print('Tuple', tuple, '\'Immutable (fixed once created)\'')
print(' ')
sentence = "I am a teacher and I love to inspire and teach people"
words_list = sentence.split()
unique_words = set(words_list)
count = len(unique_words)
print(f"Unique words: {unique_words}")
print(f"Number of unique words: {count}")