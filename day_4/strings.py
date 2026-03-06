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