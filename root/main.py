import random
while True:
    coin = random.choice(["heads", "tails"])
    while True:
        guess = input("What do you guess? (heads or tails)\n").lower()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("invalid input")
    if guess == coin:
        print("correct")
    else:
        print("incorrect")