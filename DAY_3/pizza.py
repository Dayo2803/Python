print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L ")
pepporni = input("Do you want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill = 15
    if pepporni == "Y":
        bill = 17
elif size == "M":
    bill = 20
    if pepporni == "Y":
        bill = 23
else:
    bill = 25
    if pepporni == "Y":
        bill = 28

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")
