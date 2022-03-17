import sys
height = input(("what is your height? "))
unit = input ("What would you like to conver to in or cm? ").lower()
try:
    if unit == "cm":
        print (f'Your height in cm is {(float(height) * 2.54)}')
    else:
        print (f'Your heigh in in is {(float(height) / 2.54)}')
except ValueError:
    print('Please enter a valid interger.')