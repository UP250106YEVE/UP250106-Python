# DAY 4

# Exercises day 4

# 1. Concatenate the string 'Coding', 'For', 'All'. Single string.

strings = ['Thirty', 'Days', 'Of', 'Python']
frase = ' '.join(strings)
print(frase)

# 2. Concatenate the string 'Coding', 'For', 'All' to a single string

strings = ['Coding', 'For', 'All']
frase = ' '.join(strings)
print(frase)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = 'Coding for all'

# 4. Print the variable company using print().

print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.

company = 'Coding For All'
print(company.upper())

# 7. Change all characters to lowercase letters using lower() method

company = 'Coding For All'
print(company.lower())

# 8. 

company = 'Coding For All'
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. 

text = "Coding For All"
first_word_slice = slice(0, 6)
print(text[first_word_slice])

# 10.

texto = 'Coding For All'
check = 'Coding' in texto
print(check)

# 11.

texto = 'Coding For All'
nuevo = texto.replace('Coding' , 'Python')
print(nuevo)

# 12. 

texto = 'Python For Everyone'
nuevo = texto.replace('Python For Everyone', 'Python For All')
print(nuevo)

# 13.

texto = 'Coding For All'
nuevo = texto.split(' ')
print(nuevo)

# 14.

texto = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
nuevo = texto.split(', ')
print(nuevo)

# 15. 

text = "Coding For All"
print(text[0])

# 16.

texto = 'Coding For All'
ultimo = len(texto) - 1
print(ultimo)

# 17. 
Frase  = 'Coding For All'
substring = ' '
print(Frase.index(substring))

# 18.

frase = 'Python For Ebriuan'
acronym = frase[0] + frase[7] + frase[11]
print(acronym)

# 19.

frase = 'Coding For All'
acronym = frase[0] + frase[7] + frase[11]
print(acronym)

# 20. 

frase = 'Coding For All'
index = frase[0]

# 21.

frase = 'Coding For All'
sub_string = 'F'
print(frase.index(sub_string))

# 22. 

frase = 'Coding For All People'
print(frase.rfind('i')) 

# 23.

frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))

# 24.

frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.rindex('because'))

# 25.

frase = 'You cannot end a sentence with because because because is a conjunction'
cortar = frase.find('because')
cortar = frase.rfind('because')
print(frase[:31] + frase[54:])

# 26. 

frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))

# 27.

frase = 'You cannot end a sentence with because because because is a conjunction'
cortar = frase.find('because')
cortar = frase.rfind('because')
print(frase[:31] + frase[54:])

# 28. 

frase = 'Coding For All'
print(frase.startswith('Coding'))

# 29.

frase = 'Coding For All'
print(frase.endswith('Coding'))

# 30.

frase = '   Coding For All      '
print(frase.strip(' '))

# 31.

frase1 = '30DaysOfPython'
frase2 = 'thirty_days_of_python'
print(frase1.isidentifier())
print(frase2.isidentifier())

# 32. 

listas =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon', '']
resultado = '# '.join(listas)
print(resultado)

# 33.

print("I am enjoying this challenge.\nI just wonder what is next.")

# 34.

print('Name\tAge\t\Country\tChallenge')
print('Asabeneh\t250\t\Finland\Helsinki')


# 35.

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius', radius,' is', area, 'square meters')

# 36.

a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')