# FileNotFound
try:
    file = open('a_file.txt')
except FileNotFoundError:
    file = open('a_file.txt', 'w')

print(file)
# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ["apple", "banaana"]
# fruit = fruit_list[2]

