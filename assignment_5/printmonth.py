# program to create a calander based on date and month
# Blessing Hlongwane
# HLNBLE002
# 14 March 2023

start_month = input("Enter the name of a month (e.g. January, ..., December):\n")
start_date = eval(input("Enter the start day (1 for Monday, ..., 7 for Sunday):\n"))
count = 0

if start_month == "April" or start_month == "June" or start_month == "September" or start_month == "November":
    month_range = 30
elif start_month == "February":
    month_range = 28
elif start_month == "January" or start_month == "March" or start_month == "May":
    month_range = 31
elif start_month == "July" or start_month == "August" or start_month == "October" or start_month == "December":
    month_range = 31
else:
    month_range = 1
 

if month_range >25:
    if 0 < start_date < 8: # Checks for valid input
        print(start_month)
        if month_range == 28:
            print("Mo Tu We Th Fr Sa Su\n")
        else:
            print("Mo Tu We Th Fr Sa Su")        
        # Checks where to start where index = 1 and friday = -5
        for i in range((start_date-2)*-1, month_range+1):
            if i < 1:
                if len(str(i))< 2: # If it's a single digit adjust to 2 width
                        print("  ", end=" ", sep="")
                else:
                        print("  " ,end=" ")        
                count+=1
            else:
                if len(str(i))< 2:
                        print(f" {i}", end=" ", sep="")
                else:
                        print(f"{i}", end=" ")           
                if count < 6:
                    count += 1
                else:
                    print()
                    count = 0
    else:
        print("Invalid calendar: you have either entered an incorrect month name or start day.")
else:
    print("Invalid calendar: you have either entered an incorrect month name or start day.")