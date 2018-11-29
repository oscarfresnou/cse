import random
n = random.randint(0, 10)
guesses_remaining = 4
win = False
guess = int(input("guess a number from 1 to 10:"))
while guesses_remaining > 0 and not win:
    guesses_remaining -= 1
    if guess > n:
        print("guess is too high")
        guess = int(input("guess a number from 1 to 10: "))
    elif guess < n:
        print("guess is too low")
        guess = int(input("Enter an integer from 1 to 10: "))
    elif guess == n:
        print("You guessed it!")
        win = True
    if guesses_remaining == 0:
        print("You lose! try again")

