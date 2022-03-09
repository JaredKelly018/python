arr = list(range(1,101))
for i in range(len(arr)):
    if arr[i] % 3 == 0 and not arr[i] % 5 == 0:
        arr[i] = "Fizz"
    elif arr[i] % 5 == 0 and not arr[i] % 3 ==0:
        arr[i] = "Buzz"
    elif arr[i] % 3 == 0 and arr[i] % 5 == 0:
        arr[i] = "FizzBuzz"
print(arr)

 # “Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.”


