import sys

eq = "x _ y ="
print(eq)

x = input("what does x equal? ")

y = input("what does y equal? ")

op = input("What operation whould yuou like to complete today ")
print(op)

if op == "add":
    print(x + " + " +  y + " =")
    print(float(x) + float(y))
elif op == 'sub':
    print(x + " - " +  y + " =")
    print(float(x) - float(y))
elif op == 'mult':
    print(x + " x " +  y + " =")
    print(float(x) * float(y))
elif op == 'div':
    print(x + " / " +  y + " =")
    print(float(x) / float(y))
else:
    print('operation does not exsist')
    sys.exit()

    #asdsadsad