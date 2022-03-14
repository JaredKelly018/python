eq = "x _ y ="
print(eq)

op = input("What operation whould yuou like to complete today ")
print(op)

x = input("what does x equal? ")

y = input("what does y equal? ")

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
    print('The operation ytou wish to preform does not exsist')