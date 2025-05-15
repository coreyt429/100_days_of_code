def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(*(num for num in range(30))))

def calculate(num=0, **kwargs):
    total = num
    total += kwargs.get('add', 1)
    total *= kwargs.get('multiply', 1)
    return total


print(calculate(2, add=3, multiply=5))

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']

my_car = Car(make="Nissan", model="Armada")

print(my_car.make)
