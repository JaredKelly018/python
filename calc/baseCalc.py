import sys

eq = "x _ y ="
print(eq)

op = input("Would you like to add, sub, mult, or div? ").lower()
print(op)

op = input("What operation whould yuou like to complete today ")
print(op)

if op == "add":
    x = input("what does x equal? ")
    y = input("what does y equal? ")   
    print(x + " + " +  y + " =")
    print(float(x) + float(y))
elif op == 'sub':
    x = input("what does x equal? ")
    y = input("what does y equal? ")   
    print(x + " - " +  y + " =")
    print(float(x) - float(y))
elif op == 'mult':
    x = input("what does x equal? ")
    y = input("what does y equal? ")   
    print(x + " x " +  y + " =")
    print(float(x) * float(y))
elif op == 'div':
    x = input("what does x equal? ")
    y = input("what does y equal? ")   
    print(x + " / " +  y + " =")
    print(float(x) / float(y))
else:
    print('operation does not exsist')
    sys.exit()
