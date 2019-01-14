import random
word_bank = ["Big Chungus", "Communism", "T-pose", "Thanos", "Concerned", "Flex Tape",
             "That's a lot of damage!", "Freedom", "Fear", "Skins"]
chosen_word = word_bank[random.randint(0, len(word_bank - 1))]
guesses_remaining = 12
turns = 10
while turns > 0:
    failed = 0
    
