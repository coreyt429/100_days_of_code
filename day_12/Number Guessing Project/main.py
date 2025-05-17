from random import choice
from art import logo
TURNS = {
    'e': 10,
    'h': 5
}

def greeting():
    """Prints greeting"""
    # print greeting
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100 inclusive")

def get_mode():
    # ask easy (10) or hard (5)
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()[0]
    # if invalid input, just be randomly evil and continue
    return TURNS.get(mode, choice([num for num in range(1, 11)]))

def get_guess(turns):
    """
    Function to get user input for a guess
    :param turns: int() turns remaining
    :return: int() guessed value
    """
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = False
    while not guess:
        guess = input("Make a guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print(f"Invalid guess '{guess}'")
            guess = False
    return guess

def check_guess(attempt, answer):
    """
    Function to check a guess against the answer
    :param attempt:  int() guess
    :param answer:  int() answer
    :return: bool() guess indicator
    """
    retval = False
    if attempt == answer:
        print(f"You got it! The answer was {answer}")
        retval = True
    elif attempt < answer:
        print("Too Low.")
    elif attempt > answer:
        print("Too High.")
    else:
        print("How did we get here?")
    return retval

def game():
    """
    Play game
    :return: None
    """
    greeting()
    # generate number
    random_number = choice([num for num in range(1,101)])
    turns_remaining = get_mode()
    # loop while not guessed and turns remain
    guessed = False
    while not guessed and turns_remaining:
        guess = get_guess(turns_remaining)
        guessed = check_guess(guess, random_number)
        turns_remaining -= 1

    if not guessed:
        print(f"You've run out of guesses, you lose. the number was {random_number}")

if __name__ == "__main__":
    game()