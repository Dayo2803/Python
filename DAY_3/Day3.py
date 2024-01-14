print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'. ").lower()

if road == 'left':
    option = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if option == 'wait':
        option2 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, One yellow and one blue. Which color do you choose? ").lower()
        if option2 == 'red':
            print("Its a room full of water. Game Over")
        elif option2 == 'yellow':
            print("You have found the treasure.")
        elif option2 == 'blue':
            print("You have entered a Hyde's den")
        else:
            print("You got attacked by a hungry dog.")
    else:
        print("You got attacked by an angry troll. Game Over.")
else:
    print("You fell into a hole, Game Over")