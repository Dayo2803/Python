print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("You can have a free ride")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    photo = input("Do you want your photo taken? Y or N. ")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("sorry, you have to grow taller to go on a ride.")
