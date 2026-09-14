import random
score = 0
streak = 0
while True:
    coin = random.choice(["heads", "tails"])
    while True:
        guess = input("What side of a coin?\n")
        guess = guess.lower()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("invalid input")
    if guess == coin:
        streak = streak + 1
        print("correct")
        if streak >= 5:
            score = score * 2
            print("bonus (x2 points)")
        else:
            score = score + 1
            print("+1 point")
    else:
        streak = 0
        score = 0
        print("incorrect")
        print("game over")
        print("~NEW GAME~")
    print("score:")
    print(score)
    print("streak:")
    print(streak)