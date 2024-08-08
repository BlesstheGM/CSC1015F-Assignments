# program to return value of coordinate
# Blessing Hlongwane
# HLNBLE002
# 20 April 2023

a = 1
our_array = ""
while True:
    # Ask for array until grid reaches 9
    while a < 10:
        if a == 1:
            inp = input("Enter an array:\n")
        else:
            inp = input("")
        our_array += inp + "\n"
        a += 1    
    else:
        rows = our_array.split()
        coordinate = input("Enter coordinates:\n")
         # We check whether our input has -1 If so break the loop
        if "-1" in str(coordinate):
            print("DONE")
            break
        else:       
            row = eval(coordinate[0])
            coloumn = eval(coordinate[2])
            # Find the X coordinate first then the Y coordinate
            print("Value =", rows[row][coloumn])