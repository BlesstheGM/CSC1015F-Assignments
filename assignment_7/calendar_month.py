# program to print out a calender
# Blessing Hlongwane
# HLNBLE002
# 12 April 2023

import math


def day_of_week(day, month, year):
    if month == 1 or month == 2:
        month = month + 12
        year = year - 1
    else:
        pass
    day_of_week = ( day + math.floor( 13*(month + 1) / 5 ) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400) ) % 7
    day_of_week = (day_of_week + 5) % 7 + 1
    return day_of_week


def is_leap(year):
    # Checks whether a year is a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def month_num(month_name):
    # Returns the month number of a month
    pos = 1
    for month in "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december":
        if month_name.lower() == month:
            return pos
        else:
            pos += 1
    # Your code here

def num_days_in(month_num, year):
    while month_num <= 7:
        # For months from January to June
        if month_num == 2 :
            if is_leap(year) == True:
                days_in_month = 29
                break
            else:
                days_in_month = 28
                break
        elif month_num % 2 == 0:
            days_in_month = 30
            break
        else:
            days_in_month = 31
            break
    else:
        # For months from June to December
        if month_num % 2 == 0:
            days_in_month = 31
        else:
            days_in_month = 30
    return days_in_month
        
def num_weeks(month_num, year):
    #Returns the number of weeks in a certain month dependent on year
    start_day = day_of_week(1, month_num ,year)
    leapYear = is_leap(year)
    if num_days_in(month_num, year) == 31:
        if start_day == 6 or start_day == 7:
            return 6
        else:
            return 5
    elif num_days_in(month_num, year) == 30:
        if start_day == 7:
            return 6
        else:
            return 5
    elif month_num == 2:
        if start_day == 1 and leapYear == False:
            return 4
        else:
            return 5

def week(week_num, start_day, days_in_month):
    week = ""
    end = week_num*7 - start_day + 2 
    start = end - 7
    skip_line = ""
    space = ""
    if week_num == 1:
        space = start_day
        space = " "*((space-1)*2+(space-1))  
    else:
        pass
    while end > days_in_month:
        start = end - 7
        end = days_in_month + 1
        skip_line = "\n"
        break
    else:
        pass
    week += space
    for number in range(start, end):
        if number > 0:
            # Increments the number of days in our week
            if len(str(number)) < 2:
                week += " " + str(number) + " "
            else:
                week += str(number) + " "
    week += skip_line 
    return week[:len(week)-1]

def main():
    month = input("Enter month:\n")
    year = eval(input("Enter year:\n"))
    seq = ""
    print(month.title())
    print("Mo Tu We Th Fr Sa Su")
    for number in range(1, 7):
        # Returns week sequence from weeks() function then skips a line for the next week 
        seq += str(week(number , day_of_week(1, month_num(month), year)  , num_days_in(month_num(month), year))) + "\n"
    return print(seq[:len(seq)-2]) 

if __name__=='__main__':
    main()



