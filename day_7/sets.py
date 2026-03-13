#Day_7
#Excercises level 1
print('EXCERCISES LEVEL 1')
print(' ')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print('it companies: ', it_companies)
print('A: ', (A))
print('B: ',B)
print('Age: ', age)

print('Lenght of \'it companies\': ', len(it_companies))
it_companies.add('Twitter')
print('Adding \'Twitter\' to \'it companies\': ', it_companies)
more_its = ('Intel', 'Samsung', 'Amazon', 'Apple', 'NVidia', )
it_companies.update(more_its)
print('Adding more ITs to \'it companies\': ', it_companies)
removed_item = it_companies.pop()
print('Random removed item: ', removed_item)
it_companies.remove('Samsung')
print('With \'remove()\' we can delete whatever ' \
'item we want, for example, i removed \'Samsung\': ', it_companies)
print('But if i try to remove something that does not exist in the set, it '
'simply shows \'KeyError\'')
it_companies.discard('Banana')
print('With \'discard()\' it is the same thing, the only difference is that ' \
'when your remove something that does not exist ' \
'on the set it simply continues like nothing happened '
'and it does not show the \'KeyError\' thing. For example, i tried to ' \
'remove \'Banana\' from the \'it companies\' set: ', it_companies, 'and nothing happened.')
print(' ')