import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3' '4', '5', '6', '7', '8', '9']
symbols= ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=']

print("Welcome to the pyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_num = int(input("How many numbers would you like?\n"))

password = []
for char in range(1, num_letters + 1):
    password.append(random.choice(letters))

for char in range(1, num_num + 1):
    password.append(random.choice(numbers))
    
for char in range(1, num_symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

p_password = ""
for char in password:
    p_password += char

print(f"your password is: {p_password}")