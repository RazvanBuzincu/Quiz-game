print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("No problem, maybe next time!")
    quit()

print("Okay! Let's play :) ")
score = 0

def check_answer(question, correct_answers):
    answer = input(question).lower()
    if answer in correct_answers:
        print('Correct!')
        return 1
    else:
        print(f"Incorrect! The correct answer was {' or '.join(correct_answers).capitalize()}.")
        return 0

score += check_answer("What is the capital of France? ", ["paris"])
score += check_answer("What is the capital of Germany? ", ["berlin"])
score += check_answer("What is the capital of Italy? ", ["rome"])
score += check_answer("What is the capital of England? ", ["london"])
score += check_answer("What is the capital of Belgium? ", ["brussels", "bruxelles"])
score += check_answer("What is the capital of Hungary? ", ["budapest"])
score += check_answer("What is the capital of Romania? ", ["bucharest"])

total_questions = 7
print(f"You got {score} out of {total_questions} questions correct!")
print(f"You scored {(score / total_questions) * 100:.2f}%.")
