import datetime

print("Hello. Welcome to Artisian Blockchain")
print("Press enter to start")

# Typing game
start_time = datetime.datetime.now()

text = input()

end_time = datetime.datetime.now()
score = end_time - start_time
print (score)

print("Thanks for playing")
quit()
