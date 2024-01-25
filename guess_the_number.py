import random

n=random.randint(1,4)


while True:
    guess = int(input("Enter a number"))

    if guess ==n:
        print("correct")
        break
    else:
        print("wrong guess")
        print("Guess again")
        continue








