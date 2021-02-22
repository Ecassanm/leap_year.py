year = input("Please input a year: ")
if (year % 100) == 0:
	if (year % 400) == 0:
		days = 29
		print("In the year 2000, there are 29 days in February" % (year, days))
   else:
		days = 28
		print("In the year %4d, there are %2d days in February." % (year, days))
else:
	if (year % 4) == 0:
		days = 29
		print("In the year %4d, there are %2d days in February." % (year, days))
	else:
		days = 28
		print("In the year %4d, there are %2d days in February." % (year, days))
