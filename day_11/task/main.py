from art import logo
from random import choice

def deal_card():
    """Returns a reandom card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def score_cards(hand):
    """Calculates score of a blackjack hand"""
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

while True:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()[0]
    if play_game == 'n':
        break
    print(logo)
    player_hand = [deal_card()] # one now, second in loop
    dealer_hand = [deal_card(), deal_card()]
    dealer_score = score_cards(dealer_hand)
    hit = 'y'
    bust = False
    blackjack = False
    # play payer hand
    while hit == 'y':
        player_hand.append(deal_card())
        player_score = score_cards(player_hand)
        if player_score == 21 and len(player_hand) == 2:
            blackjack = True
            break
        print(f"    Your cards: [{','.join([str(num) for num in player_hand])}], current score: {player_score}")
        print(f"    Computer's first card: {dealer_hand[0]}")
        if player_score > 21:
            bust = True
            break
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()[0]

    # play dealer hand
    while not bust and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = score_cards((dealer_hand))

    print(f"   Your final hand: [{','.join([str(num) for num in player_hand])}], final score: {player_score}")
    print(f"   Computer's final hand: [{','.join([str(num) for num in dealer_hand])}], finals score: {dealer_score}")

    if bust:
        print("You went over. You lose 😭")
    elif blackjack:
        print("Win with a Blackjack 😎")
    elif dealer_score > 21:
        print("Opponent went over. You win 😁")
    elif dealer_score == 21 and len(dealer_hand) == 2:
        # dealer blackjack
        print("Lose, opponent has Blackjack 😱")
    elif player_score > dealer_score:
        print("You win 😃")
    elif player_score < dealer_score:
        print("You lose 😤")
    else:
        print("Draw!")

