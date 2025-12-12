a = int(input("enter the value a :"))
b = int(input("enter the value b :"))
operation = input("enter the operation :")
if (operation == "add"):
    print(a+b)
elif(operation == "sub"):
    print(a - b)
elif(operation == "mul"):
    print(a * b)
elif (operation == "div"):
    print(a/b)
else:
    print("invalid input")