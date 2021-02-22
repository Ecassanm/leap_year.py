################################################################################
# Author: Emily Cassanmagnago 
# Date: 02/21/2021
# This program calculates roulette colors
# based on pocket number
################################################################################

year = input("Please input a year: ")
if (year % 100) == 0:
	if (year % 400) == 0:
		days = 29		
	else: 
		days = 28
else:
	if (year % 4) == 0:
		days = 29
	else: 
		days = 28
print("In the year %4d, there are %2d days in February." % (year, days)
