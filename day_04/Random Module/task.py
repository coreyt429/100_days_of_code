import random
# random_int = random.randint(1,10)
# print(random_int)
#
# random_float = random.random() * 100
# print(random_float)
#
# random_uniform = random.uniform(0, 10)
# print(random_uniform)

coin = ["heads", "tails"]

for flip in range(1, 11):
    print(f"Flip {flip} lands on {random.choice(coin)}")
    print(f"Flip {flip} lands on {coin[random.randint(0,1)]}")

