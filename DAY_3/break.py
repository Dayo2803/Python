def myAddition(x, y):
    print("performing the addition operation...")
    return (x + y)
def mySubtraction(x, y):
    print("performing the subtraction operation...")
    return (x - y)
def myMultiplication(x, y):
    print("performing the multiplication operation...")
    return (x * y)
def myDivision(x, y):
    print("performing the division operation...")
    if y == 0:
        print("division not possibel")
    return (x / y)
def myMenu():
    print("Main Menu...")
    print("1 > Addition operation...")
    print("2 > Subtraction operation...")
    print("3 > Multiplication operation...")
    print("3 > Division operation...")
    ch = int(input("please enter your preferred number..."))
    return ch
def calculation():
    ch = myMenu()
    num1 = int(input("Please enter the first number..."))
    num2 = int(input("Please enter the second number..."))
    if ch == 1:
        result = myAddition(num1, num2)
    elif ch == 2:
        result = mySubtraction(num1, num2)
    elif ch == 3:
        result = myMultiplication(num1, num2)
    elif ch == 4:
        if num2 == 0:
            return "division not possible"
        result = myDivision(num1, num2)
    print("So result = ", result)

calculation()        