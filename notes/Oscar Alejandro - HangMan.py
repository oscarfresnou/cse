import random
word_bank = ["Big Chungus", "Communism", "T-pose", "Thanos", "Concerned", "Flex Tape",
             "That's a lot of damage!", "Freedom", "Fear", "Skins"]
chosen_word = word_bank[random.randint(0, len(word_bank) - 1)]
guesses = 13
win_info = False
win_condition = False
correct_letter = [""]
letters_in_word = list(word_bank)
output = []
while guesses > 0:
    # Shows the hidden_word (The hint for the player)
    for letter in letters_in_word:
        if letter in correct_letter:
            output.append(letter)
        else:
            output.append("_")
    print("".join(output))
    break

    # Take an guess from a player and modify the letters guessed
