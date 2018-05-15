import datetime

print("Hello. Welcome to Artisian Blockchain")
print("\n\n")
print("Press enter to continue. Type q to quit.")
quit = input().lower().strip() == "q"


# Typing game
start_time = datetime.datetime.now()

text = input()

end_time = datetime.datetime.now()
score = end_time - start_time
print (score)

print("Thanks for playing")
