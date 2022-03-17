from tkinter.font import names


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

arr = list(range(1,101))
for i in range(len(arr)):
    if arr[i] % 3 == 0 and not arr[i] % 5 == 0:
        arr[i] = "Fizz"
    elif arr[i] % 5 == 0 and not arr[i] % 3 ==0:
        arr[i] = "Buzz"
    elif arr[i] % 3 == 0 and arr[i] % 5 == 0:
        arr[i] = "FizzBuzz"
print(arr)

names = ['Jane', 'Doe', 'Kev']
names[0] = 'John'
print(names)

vnames = ['lemo', 'bee', 'free']
print(vnames[-1])

pets= ['cat', 'dog', 'rat', 'zebra']
print(pets[0:3])


numbers = [1,2,3,4,5]
numbers.append(6)
numbers.insert(2,'this does not go here')
numbers.remove(5)
#.clear() to clear
print(numbers)
print(1 in numbers) #search for val in array
print(len(numbers)) #how many numers you have in array

#for loops
for item in numbers:
    print(item)

i=0
while i < len(numbers):
    print(numbers[i])
    i += 1

for nums in range(1,11,2):
    print(nums)

#turples are innmutable
tnumbers = (1,2,3)