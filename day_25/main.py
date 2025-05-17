# with open("weather_data.csv", mode='r') as file:
#     data = file.read().splitlines()
#
# print(data)
# import csv
#
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(type(data["temp"]))
#
# test = data.to_dict()
# print(test)
#
# temp_list = data["temp"].to_list()
#
# print(temp_list)
#
# mean = data["temp"].mean()
# print(mean)
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].max())
#
# print(data.condition)
#print(data[data.temp == data.temp.max()].to_dict())
#
# monday = data[data.day == "Monday"]
# # print(monday)
# temp = monday.temp.apply(lambda c: (c * 9/5) + 32)
# print(monday.temp.values[0], temp.values[0])
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56 ,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("squirrel_data.csv")

# print(data)
colors = data["Primary Fur Color"]
color_counts = colors.value_counts()
color_counts.to_csv("squirrel.colors.csv")
