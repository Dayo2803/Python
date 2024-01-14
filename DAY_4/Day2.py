import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_img = [rock, paper, scissors]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(game_img[choose])
c_choice = random.randint(0, 2)
print("Computer Chose:")
print(game_img[c_choice])

if choose >= 3 or choose > 0:
    print("You typed an invalid number")
elif c_choice > choose:
    print("You lose")
elif c_choice < choose:
    print("You win!")
elif c_choice == 2 and choose == 0:
    print("You win!")
elif c_choice == 0 and choose == 2:
    print("You Lose!")
elif c_choice == choose:
    print("Draw!")