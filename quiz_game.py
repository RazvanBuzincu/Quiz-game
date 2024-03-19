print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What is the capital of France? ").lower()
if answer == "paris":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of Germany ").lower()
if answer == "berlin":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of Italy? ").lower()
if answer == "rome":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of England? ").lower()
if answer == "london":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of Belgium? ").lower()
if answer == "bruxelles":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of Hungary? ").lower()
if answer == "budapest":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!!")

answer = input("What is the capital of Romania? ").lower()
if answer == "bucharest":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 7) * 100) + "%.")