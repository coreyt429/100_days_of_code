print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size.lower() == 's':
    price += 15
elif size.lower() == 'm':
    price += 20
elif size.lower() == 'l':
    price += 25
else:
    print(f"Invalid input: {size}")
if pepperoni.lower() == 'y':
    if size.lower() == 's':
        price += 2
    else:
        price += 3

if extra_cheese.lower() == 'y':
    price += 1

print(f"Your final bill is: ${price}.")