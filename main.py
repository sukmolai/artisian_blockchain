import datetime
import random

def random_sentence():
    with open("sentence_bank.txt") as f:
        lines = f.readlines()
    return random.choice(lines).strip()

print("Hello. Welcome to Artisian Blockchain")
print("\n\n")
print("Press enter to continue. Type q to quit.")
quit = input().lower().strip() == "q"

gen_sentence = random_sentence()
print(gen_sentence)

# Typing game
start_time = datetime.datetime.now()

text = input()
if text == gen_sentence:
    print("Good job fam")
else:
    print("U dun goofed")

end_time = datetime.datetime.now()
score = end_time - start_time
print (score)

print("Thanks for playing")
