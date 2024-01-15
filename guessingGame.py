import random

"""
This program will prompt the user to provide the parameter for a number guessing game. In this case,
it will be the upper limit. For example, the program will say, "Pick a number between 1 and 20,"
20 being the parameter provided by the user.

Though this is a simple program, the primary purpose of this is for me to become familiar with Python syntax.
"""


# (int) counter: tracks number of guesses it takes the user to get the right answer
counter = 1


# program greets user
print("Hello and welcome! Let's play a game!")

print("You will guess a number between 1 and an upper bound of your choosing.")

# ask user for upper limit
try:
    max = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter an integer.")

# (int) userGuess: the user's current guess
userGuess = 0
# (int) correctNumber: this number is the correct answer
correctNumber = random.randint(1, max)


# say: pick a number between 1 and [upper limit]
print("Ready! Pick a number between 1 and", max)
try:
    userGuess = int(input())
except ValueError:
    print("Invalid input. Please enter an integer.")

# loop until correct number is guessed
#
while userGuess != correctNumber:

    # if the user's guess is less than the correct number, inform the user, and get user input
    if userGuess < correctNumber:
        print("Incorrect. It is greater than", userGuess)
        print("Try again. ")
        try:
            userGuess = int(input())
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # if the user's guess is greater than the correct number, inform the user, and get user input
    if userGuess > correctNumber:
        print("Incorrect. It is greater than", userGuess)
        print("Try again. ")
        try:
            userGuess = int(input())
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # track the amount of guesses, increment by 1 after each guess
    counter += 1

#
# end of while loop, meaning the user's guess = correct number

# congratulate user and print how many guesses it took
print(userGuess, "is correct!")
print("It took you", counter, "attempts.")
