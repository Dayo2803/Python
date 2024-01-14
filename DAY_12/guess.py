import random
from art import logo

HARD_Level = 5
EASY_Level = 10

#guess number
answer = random.randint(1, 100)

def checkAnswer(guess_num, answer, turns):
    """to check if guessed number is equal to the randomly generated number"""
    if guess_num > answer:
        print("Too high")
        return turns -1
    elif guess_num < answer:
        print("Too low")
        return turns - 1
    elif guess_num == answer:
        print(f"You got it! The answer was {answer}")
        return turns - 1

def setLevel():
    """user makes a choice"""
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == 'easy':
        return EASY_Level
    elif choice == 'hard':
        return HARD_Level

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = setLevel()
    guess_num = 0
    while guess_num != answer and turns != 0:
        print(f"You have {turns} attempts remaining to guess the number")
        guess_num = int(input("Make a guess: "))

        turns = checkAnswer(guess_num, answer, turns)
    if turns == 0:
        print(f"You have run out of turns, you lose. The answer was {answer}")
        return
    else:
        print("Congratulations!, You win!")

game()