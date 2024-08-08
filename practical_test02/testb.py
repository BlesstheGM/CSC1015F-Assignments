# program to count the number of adjacent pairs of multiples of 4 in a sequence
# Blessing Hlongwane
# HLNBLE002
# 03 April 2023

count = ""
option = ""
pair = 0
start = 0
while option != "DONE":
    option = input("Enter a number (or 'DONE' to finish):\n")
    count += option + " "
else:
    print("Number of adjacent pairs of multiples of 4:", end=" ")
    
numbers = count[:len(count)-4]
for number in numbers:
    if number == " ":
        space = numbers[start:].find(" ")
        end = space + start + 1
        f = numbers[start:end]
        c = (len(f)-1)
        if eval(f) % 4 == 0:
            position = start
            if numbers[position] == numbers[position+c+1]:
                pair += 1           
        start += space + 1
print(pair,end=".")