from hangman_words import word_list
from hangman_art import  logo, stages
import random
chosen_word = random.choice(word_list)

max_lives = 6
lives_remaining = max_lives

answer_key = list(chosen_word)
current_word = list('_'*len(answer_key))

win = False
lose = False
print(logo)
guesses = []
while not win and not lose:
    print(stages[lives_remaining])
    print(f"{'*'*14} {lives_remaining} / {max_lives} LIVES Left {'*'*14}")
    print(f"already guessed: {' '.join(guesses)}")
    print(f"Word to guess: {' '.join(current_word)}")
    guess = input('Guess a letter: ')
    guess = guess.strip().lower()[0]
    guesses.append(guess)
    if guess in answer_key:
        for idx, char in enumerate(answer_key):
            if char == guess:
                current_word[idx] = char
        if current_word == answer_key:
            win = True
    else:
        lives_remaining -= 1
        if lives_remaining == 0:
            lose = True
        print(f"You guessed {guess} which is not in the word. You lose a life.")

if lose:
    print(f"You Lose: the word was {''.join(answer_key)}")

if win:
    print("You win! the word was {''.join(answer_key)")


