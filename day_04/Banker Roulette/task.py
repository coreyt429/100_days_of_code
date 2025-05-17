import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    payer = random.choice(friends)
    friends.pop(friends.index(payer))
    print(f"{day} {payer} pays")
