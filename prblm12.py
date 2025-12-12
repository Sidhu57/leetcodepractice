salary = int(input("enter the salary :"))
age = int(input("enter the age :"))
if(salary >=20000 or age <= 25):
    loanamount = int(input("enter the required amount :"))
else:
    print("your not eligible for the loan")
if (loanamount <= 50000):
        print("You are eligible for the loan")
else:
        print("Maximum loan amount allowed is 50,000")