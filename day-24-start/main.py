import os
file_path = os.fspath('../../OneDrive/Desktop/my_file.txt')
print(file_path)
with open('../../OneDrive/Desktop/my_file.txt') as file:
    data = file.read()
    print(data)
