import sys

try:
    height = input(("what is your height? "))
except ValueError:
    print('Please enter a valid interger.')

unit = input ("What would you like to conver to in or cm? ").lower()
if unit == "cm":
    print (f'Your height in cm is {(float(height) * 2.54)}')
else:
    print (f'Your heigh in in is {(float(height) / 2.54)}')

