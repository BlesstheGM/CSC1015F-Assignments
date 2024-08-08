# programto print out the numbers n to n+41 as 6 rows of 7 numbers
# Blessing Hlongwane
# HLNBLE002
# 09 March 2023

number = eval(input("Enter a number between -6 and 2:\n"))

if -6 < number < 2:  # Checks for valid input  
        for a in range(0, 42, 7):
                for b in range(number, number+7, 1): 
                        # Prints the first 7 terms horizontally starting from number(our input).
                        if len(str(a+b))< 2:
                                print(" " ,a+b, end=" ", sep="")
                        else:
                                print(a+b, end=" ")
                print("") # starts a second row of 7 terms starting from value 8
else:
        print("Invalid input! The value of 'n' should be between -6 and 2.")      
        