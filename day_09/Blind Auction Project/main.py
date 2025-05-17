from art import logo
print(logo)

bidders = {}

more_bidders = True
while more_bidders:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    # TODO-2: Save data into dictionary {name: price}
    bidders[name] = int(bid)
    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()[0] == 'y'
    print("\n" * 20)

# TODO-4: Compare bids in dictionary
high_bid = max(bidders.values())
winners = [name for name, bid in bidders.items() if bid == high_bid]

if len(winners) == 1:
    print(f"The winner is {winners[0]} with a bid of ${high_bid}")
else:
    print(f"{', '.join(winners)} all bid ${high_bid}, rebid!")





