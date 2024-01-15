
from game_data import data

def random_account():
    """generate a random account from the data"""
    choice = random.choice(data)
    print(choice)

random_account()