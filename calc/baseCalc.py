eq = "x _ y ="
print(eq)

op = input("What operation whould yuou like to complete today ")
print(op)

if op == "addation" or "add" or "a" or"+":
    x = input("what is the first number you would like to add? ")
    print(x + " +" + " y" + " =")
    y = input("what is the second number you would like to add? ")
    print(x + " + " +  y + " =")
    print(float(x) + float(y))

else:
    print("try agin.")
