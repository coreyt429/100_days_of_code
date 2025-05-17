enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


my_global_var = 3

def my_function():
    # This works no problems
    print(my_global_var)

my_function()


def my_function2():
    global my_global_var
    my_global_var = 2
    print(my_global_var)

my_function2()

# This will cause a NameErrorr
print(my_global_var)


