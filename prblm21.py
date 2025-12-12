a = []
print("enter the 7 numbers")
for i in range (7):
    num = int(input("enter the numbers " + str(i+1)))
    a.append(num)
print(a)

sum = 0
for i in a:
    sum = sum +i
print(sum)