year = input("Please input a year: ")
if (year % 100) == 0:
	if (year % 400) == 0:
		print("In the year %4d, there are 29 days in February." % (year))
	else:
		print("In the year %4d, there are 28 days in February." % (year))
else:
	if (year % 4) == 0:
		print("In the year %4d, there are 29 days in February." % (year))

	else:
		print("In the year %4d, there are 28 days in February." % (year))
