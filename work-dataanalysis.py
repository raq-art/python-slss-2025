# Data Analysis
# Author: Rachel
# Open the file

# Analyse the data provided in class


def main():
    #     # do your work in here
    #     file = open("data/NYC_Central_Park_weather_1869-2022.csv")
    #     print("There are a total of 56245 data points.")

    #     total_rain = 0
    #     _ = file.readline()  # gets rid of header

    #     # average rainfall
    #     for line in file:
    #         info = line.split(",")
    #         avg_rain = float(info[1])
    #         total_rain += avg_rain

    #     print(f"the average rainfall is: {total_rain / 56245}")

    # temperature
    # file = open("data/NYC_Central_Park_weather_1869-2022.csv")
    # _ = file.readline()  # gets rid of header
    # Total_temp = 0

    # for line in file:
    #     info = line.split(",")

    #     if info[4]:
    #         avg_temp = float(info[4])
    #         Total_temp += avg_temp
    #         Avg_min_temp = Total_temp / 56245

    # print(f"The average minimum temperature is: {Avg_min_temp} F")
    # print(
    #     f"The average temerature in celsius is : {(Avg_min_temp - 32) * 0.5555555555555555555} C"
    # )

    # june temperature
    file = open("data/NYC_Central_Park_weather_1869-2022.csv")
    _ = file.readline()  # gets rid of header

    total_max_temp = 0

    for line in file:
        info = line.split("-")

        if info[1] == "06":
            max = line.split(",")
            if max[5]:
                max_temp = float(max[5])
                total_max_temp += max_temp
    Average_max_temperature = total_max_temp / 4590
    print(f"The average max temperature in June is {Average_max_temperature}")

    file.close()


if __name__ == "__main__":
    main()
