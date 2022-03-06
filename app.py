from pydoc import doc
import select


gender = input('What prouns would you like me to use for you?')
print('You have chosen ' + gender + '.')

birth_year = input('Enter your birth year:')
age = 2022 - int(birth_year)
print(age)

x = input('Please select your first  number')
y = input('Please select your second number')
sum = float(x) + float(y)
print('The sum is `' +str(sum))

upper_case = 'Make Me all Upper case please or Lowe 9'
print(upper_case.upper())
print(upper_case.lower())
print(upper_case.find("or")) #tells you index location
print('all' in upper_case) #checks to see if str is there
print(upper_case.replace('Make', 'mae'))

print(12/3) # returns floatig poiunt
print(12//5) #returns interger
print(10 % 3) #remainder
print(10 **3) #power of


