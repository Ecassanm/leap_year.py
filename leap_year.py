################################################################################
# Author: Emily Cassanmagnago 
# Date: 02/21/2021
# This program calculates roulette colors
# based on pocket number
################################################################################

year = int(input("Please input a year: "))
if (year % 100) == 0:
    if (year % 400) == 0:
        days = 29
        print("In the year", year, ", there are", days, "days in February.")
    else:
        days = 28
        print("In the year", year, ", there are", days, "days in February.")
else:
    if (year % 4) == 0:
        days = 29
        print("In the year", year, ", there are", days, "days in February.")
    else:
        days = 28
        print("In the year", year, ", there are", days, "days in February.")
