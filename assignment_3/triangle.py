# program to calculate the area of a triangle
# Blessing Hlongwane
# HLNBLE002
# 23 February 2023

import math 

first_side = float(input("Enter the length of the first side: "))
second_side = float(input("Enter the length of the second side: "))
third_side = float(input("Enter the length of the third side: "))
s = (first_side + second_side + third_side)/2

if first_side > third_side or second_side > third_side:
    print("Error: The input does not describe a triangle.")
else: 
    area = math.sqrt(s * (s-first_side) *(s-second_side) * (s-third_side))
    if area == 0:
        print("Error: The input does not describe a triangle.")
    else:
        print("The area of the triangle with sides of length", end=" ")
        print(first_side, end=" and ")
        print(second_side, end=" and ")
        print(third_side, end=" is ")
        print(round(area, 2), ".", sep="") # Rounds off to 2 decimal places    



