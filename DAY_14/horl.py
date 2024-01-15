import random
from art import logo, vs
from game_data import data

def random_account():
    """generate a random account from the data"""
    return random.choice(data)

def format_data(account):
    """make the data a printable one"""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name} is a {description} from {country}"

def checkAnswer(guess, a_followers, b_followers):
    """check who has more followers"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    

def game():
    print(logo)
    score = 0
    game_true = True
    a_account = random_account()
    b_account = random_account()

    while game_true:
        a_account = b_account
        b_account = random_account()

        while a_account == b_account:
            b_account = random_account()

        print(f"Compare A: {format_data(a_account)}.")
        print(vs)
        print(f"Against B: {format_data(b_account)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = a_account["follower_count"]
        b_follower_count = b_account["follower_count"]
        is_correct = checkAnswer(guess, a_follower_count, b_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_true = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
