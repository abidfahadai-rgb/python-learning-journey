import random

# Generate random toss - tails = 0, heads = 1
coin1 = random.randint(0,1)
coin2 = random.randint(0,1)

if coin1 == 0:
    print("Coin 1: Tails")
elif coin1 == 1:
    print("Coin 1: Heads")

if coin2 == 0:
    print("Coin 2: Tails\n")
elif coin2 == 1:
    print("Coin 2: Heads\n")

if coin1 == 1 and coin2 == 1:
    print("Spinner wins! Two heads!")
elif coin1 == 0 and coin2 == 0:
    print("Spinner loses! Two tails!")
else:
    print("Throw again!")

print("\nThanks for playing!")