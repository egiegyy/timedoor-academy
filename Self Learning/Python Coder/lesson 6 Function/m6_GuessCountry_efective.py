questions = {
    #questions : answer
    "By Size, what is the largest country in the world?": "Russia",
    "Which country has a unicorn as its national animal?": "Scotland",
    "In which country would you find the currency Bath?": "Thailand"
}

def check_guess():
    global score
    still_guessing = True
    attempt = 0
    for question, answer in questions.items():
        print(question)
        while still_guessing and attempt < 3:
            guess = input("Guess: ")
            if guess.lower() == answer.lower():
                print("Correct answer!")
                score += 1
                still_guessing = False
            else:
                if attempt < 2:
                    print("Wrong answer!")
                attempt += 1
        still_guessing = True
        attempt = 0

score = 0
print("Guess the Country!")
check_guess()
print("Your score is " + str(score))