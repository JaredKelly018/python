
 # “Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.”

#declare var and gen number list
for num in range(1,101):
# In order for FizzBuzz to be printed FizzBuzz has be printed first otherwise multiples of 3 and 5 will have already been repleaced
    if num % 15 == 0: # if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
#order of the elif do not matter much as they wont casue any logic issues
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)