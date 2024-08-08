# proogram to determine a program print the 7th term on one line
# Blessing Hlongwane
# HLNBLE002
# 07 March 2023

number = eval(input("Enter the start number:\n"))
last = number + 7 # Last term

if ( -6 < number < 93 ):
    for i in range(number, last):
        # When value is 1 digit
        if len(str(i)) < 2: 
            print("",i, end=" ", sep=" ")
        # When value is 2 digits
        else: 
            print(i, end=" ") 
        
    