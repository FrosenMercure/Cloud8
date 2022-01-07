import decimal

a = decimal.Decimal (input("Please Imput The First Number: "))

d = (input("Please Input Any One of The Four(+ - * /):"))

b = decimal.Decimal (input("Please Input The Second Number: "))

if d == '+':
    print("The result is: ", a+b)
    if d == '-':
        print("The result is: ", a-b)
        if d == '*':
            print("The result is: ", a*b)
            if d == '/':
                print("The result is: ", a/b)
else:
    print("Please Use One From + - x ÷")

input("Press Any Key to Quit")