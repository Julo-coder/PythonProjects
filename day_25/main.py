import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # print(data["temp"].mean())
#
# # print(data["temp"].max())
# # Get data in Colomn
#
#
# # Get the name of day with max temperature
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# #
# # fahrenheit_temp = (int(monday.temp) * 1.8) + 32
# # print(fahrenheit_temp)
#
# data_dict = {
#     "student": ["Ania", "Kasia", "Mirek"],
#     "points": [76, 74, 68]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data")

data = pandas.read_csv("squirrel_data.csv")
grey_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
red_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "fur_color": ["Grey", "Red", "Black"],
    "count": [grey_fur_count, red_fur_count, black_fur_count]
}

sq_data = pandas.DataFrame(data_dict)
sq_data.to_csv("squirrel_fur_count.csv")
