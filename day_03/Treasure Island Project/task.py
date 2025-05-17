print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print()
game_over = False
win = False
answer = input("you have come to a crossroads and must choose [L]eft or [R]ight: ")
if answer.lower()[0] == 'l':
    print("You proceed safely down the path to the left")
else:
    print("You fell in a bottomless hole.  GAME OVER")
    game_over = True

if not game_over:
    answer = input("you approach a flooded river [S]wim or [W]ait: ")
    if answer.lower()[0] == 'w':
        print("You wait patiently as the flood waters recede and walk safely across the rivebed")
    else:
        print("Attacked by trout.  GAME OVER")
        game_over = True

if not game_over:
    answer = input("You have arrived at 3 doors, choose one to enter [R]ed, [Y]ellow, or [B]lue ")
    if answer.lower()[0] == 'r':
        print("Burned by fire.  GAME OVER")
        game_over = True
    elif answer.lower()[0] == 'b':
        print("Eaten by beasts.  GAME OVER")
        game_over = True
    elif answer.lower()[0] == 'y':
        print("You proceed into the dark chamber an attempt to light a torch")
        win = True
    else:
        print("Failing to choose a door, you leaned against the invisible door and slid down the infinite water slide. GAME OVER")
        game_over = True

if win:
    print("""
    With your torch lit, you realize you are in the treasure chamber:
    
    
                               _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
    
    
    You Win!!!!
    """)