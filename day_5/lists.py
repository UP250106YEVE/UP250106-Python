#Day_5
#Excercises level 1
lst = []
print('Empty list: ',lst)
brands = ['Porsche', 'Volkswagen', 'Audi', 'BMW', 'Volvo', 'Ford']
print('My list: ',brands)
print('Lenght of my list: ', len(brands))
first = brands[0]
print('The first item is: ',first)
middle = brands[2]
print('The middle item is: ',middle)
last = brands[5]
print('The last item is: ',last)

mixed_data_types = ['Yexuanj', 18, 1.70, 'Engaged', 'Jalisco']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('New list: ', it_companies)
print('Number of companies: ', len(it_companies))
print('First company: ', it_companies[0])
print('Middle company: ', it_companies[3])
print('Last company: ', it_companies[6])

it_companies_copy = it_companies.copy()
it_companies_copy.remove('Google')
print('Modified list: ', it_companies_copy)

it_companies.append('IT')
print('Adding \'IT\' to the list: ', it_companies)
it_companies.insert(3, 'IT')
print('Putting \'IT\' in the middle of the list: ', it_companies)

it_companies_copy_2 = it_companies.copy()
it_companies_copy_3 = it_companies.copy()

it_companies_copy[1] = 'GOOGLE'
print('One company in uppercase: ', it_companies_copy)
str = '#; '
it_companies_copy.extend(str)
print('List with a \'#; \' string: ', it_companies_copy)
does_exist = 'Oracle' in it_companies
print('Does \'Oracle\' exists in the list? ', does_exist)
it_companies.sort()
print('Sort list: ', it_companies)
it_companies.sort(reverse=True)
print('Reversed list: ', it_companies)
slice_out = it_companies_copy_2[0:3]
print('Slicing out the first 3 companies: ', slice_out)
slice_out_2 = it_companies_copy_2[6:9]
print('Slicing out the last 3 companies: ', slice_out_2)

del it_companies_copy_2[3]
print('Removing first \'IT\' which is also the middle one: ', it_companies_copy_2)

del it_companies_copy_2[7]
print('Removing last \'IT\': ', it_companies_copy_2)

it_companies_copy_3.clear()
print('Deleting the \'IT\' companies list: ', it_companies_copy_3)