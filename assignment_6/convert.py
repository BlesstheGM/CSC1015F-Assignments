# program  that accepts input of a date and outputs the same information in a long form
# Blessing Hlongwane
# HLNBLE002
# 23 March 2023

date_and_time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

# Slicing our minutes, hour, day of month, month and year.
minutes = date_and_time[14:]
hour = date_and_time[11:13] 
day_of_month = int(date_and_time[8:10])
month = date_and_time[5:7]
year = date_and_time[2:4] 

count = 1
hour = int(hour)
# Searching for month that matches with sliced month number
for name in "January", "February" , "March" , "April" , "May", "June", "July" , "August" , "September", "October" , "November" , "December":
    if int(count) == int(month):
        name_of_month = name
        break
    else:
        count +=1  

if hour > 12:
    hour = hour - 12
    day = "pm"
elif hour == 0:
    hour = 12
    day = "am"
elif hour == 12:
    hour = 12
    day = "pm"
else:
    hour = hour
    day= "am"
# Identifying when to prefix st, nd, rd and th
if day_of_month == 1 or day_of_month == 21:
    month_suffix = "st"
elif day_of_month == 2 or day_of_month == 22:
    month_suffix = "nd"
elif day_of_month == 3 or day_of_month == 23:
    month_suffix = "rd"
else:
    month_suffix = "th"
    
print("{0}:{1} {2} on the {3}{4} of {5} '{6}".format(hour, minutes, day, day_of_month, month_suffix, name_of_month, year))