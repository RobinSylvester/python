# import csv
#
# with open("weather_data.csv") as f:
#     temperature = []
#     data = csv.reader(f)
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
temperature = data["temp"].tolist()
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
far_temp = (int(monday.temp) * 1.8) + 32
print(far_temp)
