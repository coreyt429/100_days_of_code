# Functions with input

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    print("Isn't the weather nice")


greet_with_name(name="Jack Bauer", location="Tulsa")

greet_with_name(location="Tulsa", name="Jack Bauer")
