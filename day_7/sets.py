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