import random
word_bank = ["Big Chungus", "Communism", "T-pose", "Thanos", "Concerned", "Flex Tape",
             "That's a lot of damage!", "Freedom", "Fear", "Skins"]
chosen_word = word_bank[random.randint(0, len(word_bank) - 1)]
guesses = 12
turns = 10
win_info = False
win_condition = False
correct_letter = []
c_word = list(chosen_word)


