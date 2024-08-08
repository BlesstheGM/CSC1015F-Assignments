import os.path
anagrams = []

try:
    my_file = open("UCT LMH.txt", "r")
    my_file.close()
    numbers = []
    for line in my_file:
        numbers.append(line[2:13]) 
    print(numbers)
except:
    print("Sorry, could not find file")