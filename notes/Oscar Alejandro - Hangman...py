import random
import sys


wordList = [
    "lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
    "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",\
           "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",\
           "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
letter_storage = []


def beginning():
    print("Hello Mate!\n")

    while True:
        name = input("Please enter Your name\n").strip()

        if name == '':
            print("You can't do that! No blank lines")
        else:
            break


beginning()


def new_func():
    print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        game_choice = input("Would You?\n").upper()

        if game_choice == "YES" or game_choice == "Y":
            break
        elif game_choice == "NO" or game_choice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue


new_func()


def change():

    for not letter in secretWord:
        guess_word.append("-")

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)


def guessing():
    guess_taken = 1

    while guess_taken < 10:

        guess = input("Pick a letter\n").lower()

        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was %s",   secretWord)


change()
guessing()

print("Game Over!")
