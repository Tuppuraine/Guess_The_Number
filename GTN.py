import random

def game():
    answer = random.randint(0, 100)  # generate answer
    tries = 0 #generate a counter
    while True:
        try:
            tries += 1 #adding a counter to tries
            question = int(input("Guess a number between 0-100: "))  #ask the number
            if (answer-question) > 10 or (answer-question) < -10:
                print("Guessed number is off more than 10, try again!")
            elif (answer - question) < 5 and (answer-question) > 0 or (answer-question) > -5 and (answer-question) < 0:
                print("Guessed number is off less than 5, try again!")
            elif (answer-question) < 10 and (answer-question) > 0 or (answer-question) > -10 and (answer-question) < -0:
                print("Guessed number is off less than 10, try again!")
            elif answer == question:
                if tries == 1:
                    print("You guessed it in", tries, "try")
                else:
                    print("You guessed it in", tries, "tries")
                break
        except ValueError: #removing ValueError possibility
            print("Please input integer only")

while True:
    play = str(input("Would you like to guess the number? (Y/N) "))
    if play == "y":
        game()
    elif play == "n":
        break