import random

test_seed = int(input("create a seed number: "))
random.seed(test_seed)

n = random.randint(0, 1)
if n == 1:
    print("Heads")
else:
    print("Tails")