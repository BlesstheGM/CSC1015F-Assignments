# program output a histogram
# Blessing Hlongwane
# HLNBLE002
# 20 April 2023

marks = input("Enter a space-separated list of marks:\n").split()

# Creating my different lists for each category
first = []
second_plus = []
second_minus = []
third = []
fail = []

for number in marks:
    number = eval(number)
    # Categorising my marks
    if number < 50:
        fail.append(number)
    elif 50 <= number < 60:
        third.append(number)
        
    elif 60 <= number < 70:
        second_minus.append(number)
        
    elif 70 <= number < 75:
        second_plus.append(number)
        
    elif number >= 75:
        first.append(number)
    else:
        pass
  
    
my_lists = {'1 ':first, '2+':second_plus, '2-':second_minus, '3 ':third, 'F ':fail}
for index in my_lists.keys(): # Fetching the keys from the dictionary
    print("{}|".format(index), end="")
    print("X" * len(my_lists[index])) # Print X times the number of itimes in the list