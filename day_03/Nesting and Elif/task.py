print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    price = 17
    if age <= 12:
        price = 5
    elif age <= 18:
        price = 7
    print(f"You can ride the rollercoaster, please pay ${price}")
else:
    print("Sorry you have to grow taller before you can ride.")
