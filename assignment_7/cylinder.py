# program to calculate area and volume
# Blessing Hlongwane
# HLNBLE002
# 12 April 2023

import math

def circle_area(diameter):
    area = 1/4*math.pi*diameter**2 # calculates area
    return area
    
def cylinder_volume(diameter, height):
    volume = circle_area(diameter) * height # Returns area then multiplies with height
    return volume

def main():
    diameter = eval(input("Enter diameter: \n"))
    height = eval(input("Enter height: \n"))
    print ("The volume of the cylinder is {:.2f} ".format(cylinder_volume(diameter, height)))
    
if __name__ == "__main__":
    main()