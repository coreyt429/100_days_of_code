from art import logo, vs
from game_data import data
from random import shuffle
"""
{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
}
"""

def banner():
    """clear screen and display banner"""
    print('\n'*20)
    print(logo)

def show_vs():
    """display vs art"""
    print(vs)

def display_item(items, key):
    """Display item"""
    item = items[key]
    print(f"Compare {key}: {item['name']}, {item['description']}, from {item['country']}")

def get_guess(items):
    """get user guess"""
    display_item(items, 'A')
    show_vs()
    display_item(items, 'B')
    return input("Who has more followers? Type 'A' or 'B': ")

if __name__ == "__main__":
    # shuffle data to start
    shuffle(data)
    # init score to 0
    score = 0
    # pop first two data items for first comparison
    comparison = {
        'A': data.pop(0),
        'B': data.pop(0),
    }
    # game on
    game_over = False
    # loop until game over
    while not game_over:
        # show banner
        banner()
        # if we have a score then the last guess was right
        if score > 0:
            print(f"You're right! Current score {score}")
        # get the next guess
        guess = get_guess(comparison)
        # follower_count for guess
        # invalid guesses get 0, and end the game
        guess_count = comparison.get(guess, {'follower_count': 0})['follower_count']
        # follower_count for highest comparison
        max_count = max(comp['follower_count'] for comp in comparison.values())
        # if the guess is not the higher value
        if guess_count < max_count:
            # game over
            game_over = True
            continue
        # correct answer, increment score
        score += 1
        # shuffle the deck again - the two in comparison
        shuffle(data)
        # add comp A to the end of the data
        data.append(comparison['A'])
        # move B to A
        comparison['A'] = comparison['B']
        # pull B from front of data
        comparison['B'] = data.pop(0)

    print(f"Sorry, that's wrong. Final score {score}")



