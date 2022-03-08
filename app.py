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

#ask for weight
weight = input('Please enter your weight: ')
#ask Kg pr Lbs
weightType = input('Is your weight in Kg or Lbs: ').lower()
#do maths
if weightType == "lbs":
    print(float(weight) / 2.205)
else:
    print(float(weight) * 2.205)


i = 1
while i <= 10:
    print(i * '[]')
    i = i + 1

height = input(("what is your height? "))
unit = input ("What would you like to conver to in or cm? ").lower()
if unit == "cm":
    print (float(height) * 2.54)
else:
    print (float(height) / 2.54)
    