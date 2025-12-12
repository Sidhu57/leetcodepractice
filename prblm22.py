a = []

print("Enter 5 numbers:")

for i in range(5):
    num = int(input("Enter number " + str(i+1) + ": "))
    a.append(num)

for num in a:
    cube = num*num*num
    print("number is :", num, "and the cube of the", num, "is :", cube)
