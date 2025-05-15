import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

player_choice = ''
while not isinstance(player_choice, int):
    player_choice = input("Choose: 0 Rock, 1 Paper, 2 Scissors [0, 1, 2]:\n")
    try:
        player_choice = int(player_choice)
    except ValueError:
        print("invalid input, please enter 0, 1, or 2")
        pass
    if player_choice not in [0, 1, 2]:
        print("invalid input, please enter 0, 1, or 2")
        player_choice = ''

computer_choice = random.randint(0,2)

print(f"Player:\n{moves[player_choice]}")
print(f"Computer:\n{moves[computer_choice]}")
difference = player_choice - computer_choice
if difference == 0:
    print("Tie Game")
elif difference in [1, -2]:
    print("Player wins")
elif difference in [-1, 2]:
    print("Computer wins")
else:
    print(f"We didn't handle this situation {player_choice} - {computer_choice} = {difference}")


