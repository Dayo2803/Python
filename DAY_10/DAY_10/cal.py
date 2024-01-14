from art import logo
print (logo)


# def add(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def mul(n1, n2):
#     return n1 * n2

# def div(n1, n2):
#     return n1 / n2

# operands = {
#     "+": add,
#     "-": sub,
#     "*": mul,
#     "/": div,
# }

# cal_end = False
# while not cal_end:
#     first_number = int(input("What's the first number?: "))

#     for sym in operands:
#         print(sym)

#     sym_oper = input("Pick an operation from the line above: ")
#     second_number = int(input("What's the second number?: "))
#     cal_func = operands[sym_oper]
#     answer = cal_func(first_number, second_number)

#     print(f"{first_number} {sym_oper} {second_number} = {answer}")
#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") != "y":
#         cal_end = True
#     else:
#         first_number = answer

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operands = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

#recursion
def calculator():
    print(logo)
    cal_end = True
    while cal_end:
        first_number = float(input("What's the first number?: "))
        for sym in operands:
            print(sym)
        sym_oper = input("Pick an operation from the line above: ")
        
        second_number = float(input("What's the second number?: "))
        cal_func = operands[sym_oper]
        answer = cal_func(first_number, second_number)

        print(f"{first_number} {sym_oper} {second_number} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            first_number = answer
        else:
            cal_end = False
            calculator()


calculator()
    # sym_oper = input("Pick another operation from the line above: ")
    # numb3 = int(input("What's the next number?: "))
    # cal_func = operands[sym_oper]
    # answer2 = cal_func(cal_func(first_number, second_number), numb3)

    # print(f"{answer} {sym_oper} {numb3} = {answer2}")