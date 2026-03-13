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

mixed_data_types = ['Yexuanj', 18, 1.70, 'Engaged', 'Aguascalientes']

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

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB'] 
total_end = front_end + back_end
print('Joinig two lists: ', total_end)

full_stack = total_end.copy()
full_stack.insert(5, 'Python')
print('Adding \'Python\': ', full_stack)
full_stack.insert(6, 'SQL')
print('Adding \'SQL\': ', full_stack)

#Excercises level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print('Ages of students: ', ages)

ages.sort()
min_age =ages[0]
max_age = ages[-1]
print('Minimum age: ', min_age)
print('Maximun age: ', max_age)

ages.extend([min_age, max_age])
ages.sort()
print('Adding two more ages: ',ages)
a = len(ages)
median = (ages[a//2-1] + ages[a//2]) / 2

average = sum(ages) / a

age_ramge = max_age - min_age
diff_min = abs(min_age - average)
diff_max = abs(max_age - average)
print(f'Median: {median}, Average: {average}, Range: {age_ramge}')
print(f'Min diff: {diff_min}, Max diff: {diff_max}')