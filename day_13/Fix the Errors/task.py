try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have typed an invalid number, try again")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
