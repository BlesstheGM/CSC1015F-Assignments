# program to output the 7th term on every new line
# Blessing Hlongwane
# HLNBLE002
# 07 March 2023

number = eval(input("Enter a number:\n"))

my_range = range(number, number + 41, 7)
if (-6 < number < 2):
    for i in my_range:
        # When value is 1 digit
        if len(str(i)) < 2: 
            print("" ,i)
        # When value is 2 digits
        else: 
            print(i) 