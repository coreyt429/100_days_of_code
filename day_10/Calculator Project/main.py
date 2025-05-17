from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def clear():
    print('\n'*25)


restart = True
register = 0
while True:
    if restart:
        clear()
        print(logo)
        register = 0
        num_1 = float(input("What is the first number?: "))
    else:
        num_1 = register
    for key in operators:
        print(key)
    operation = input("Pick an operation: ")
    num_2 = float(input("What is the next number?: "))
    register = operators[operation](num_1, num_2)
    print(f"{num_1} {operation} {num_2} = {register}")
    response = input(f"Type 'y' to continue calculating with {register}, or type 'n' to start a new calculation: ")
    restart = response.lower()[0] == 'n'
    if response.lower()[0] in 'xq':
        break

