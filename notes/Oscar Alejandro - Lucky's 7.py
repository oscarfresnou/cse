import random
roll_again = "yes"
money = 15
rounds = 0
while money > 0:
    print("rolling dice...")
    Dice_1 = random.randint(1, 6)
    Dice_2 = random.randint(1, 6)
    print("the values are...")
    print(Dice_1)
    print(Dice_2)
    rounds += 1
    money -= 1
    myrole = (Dice_1 + Dice_2)
    if myrole == 7:
        money += 5
        print("Your roll was a 7 you earned )( 4 dollars")
    elif myrole != 0:
        print("Sorry your roll wasn't 7. You lose a 1 dollar")
    elif money != 0:
        print("sorry you do not have anymore money in your pot")
print("sorry you loser. you played %d rounds" % rounds)
