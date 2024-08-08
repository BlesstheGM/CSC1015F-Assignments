# program to identify number of adjacent pairs
# Blessing Hlongwane
# HLNBLE002
# 17 April 2023

sentence = ""
where = 0
pairs = 0
sequence = ""
while sentence != "DONE":
    sentence = input("Enter a string (or 'DONE' to terminate):\n")
    sequence += sentence + ","
    
my_list = sequence.split(",")
for character in my_list:
    if my_list[where].istitle() and my_list[where+1].istitle():
        pairs += 1
    where += 1
        
print("Number of pairs of adjacent proper nouns: ", end="")
print(pairs, end=".")