print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2
tolowercase = combine_name.lower()

t = tolowercase.count("t")
r = tolowercase.count("r")
u = tolowercase.count("u")
e = tolowercase.count("e")

true = t + r + u + e

l = tolowercase.count("l")
o = tolowercase.count("o")
v = tolowercase.count("v")
e = tolowercase.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and fanta ")
elif love_score >= 40 or love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")