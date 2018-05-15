import datetime
import random

def random_sentence():
    with open("sentence_bank.txt") as f:
        lines = f.readlines()
    return random.choice(lines)

print("Hello. Welcome to Artisian Blockchain")
print("\n\n")
print("Press enter to continue. Type q to quit.")
quit = input().lower().strip() == "q"

print(random_sentence())

# Typing game
start_time = datetime.datetime.now()

text = input()

end_time = datetime.datetime.now()
score = end_time - start_time
print (score)

print("Thanks for playing")
