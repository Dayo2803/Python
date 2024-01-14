import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameasCSV = input("Give me everybody's names, seperated by a coma ")
names = nameasCSV.split(", ")
name_list = len(names)
choice = random.randint(0, name_list - 1)
pay = names[choice]
print(pay + " is going to buy the meal today")  
