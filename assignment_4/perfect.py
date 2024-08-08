# proogram to determine a perfect number
# Blessing Hlongwane
# HLNBLE002
# 07 March 2023

number = eval(input("Enter a number:\n"))
my_range = range(1, number) #Creates a range of numbers
new = 0

print("The proper divisors of", number, "are:\n", end="")
for n in my_range:
    if number % n == 0:
        print(n, end=" ")
        new += n # sum of the divisors
        
print("\n")
if new == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")