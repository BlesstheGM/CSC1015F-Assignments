# program that outputs an input as a comma-separated list
# Blessing Hlongwane
# HLNBLE002
# 23 March 2023

sentence = input("Enter a sentence:\n")
start = 0

print("The word list: ", end="")
for space in sentence:
    if space == " ":
        position = sentence[start:].find(" ") # Finding the position of a space character
        last_position = position + start 
        print(sentence[start:last_position].lower(), end=", ") # Print word upto space character
        start += position + 1 # Increment start position where we found space the original start position
        
space_from_reverse = sentence[::-1].find(" ")
if space_from_reverse == -1:
    print(sentence.lower(), end=".")
else:
    print(sentence[-space_from_reverse::].lower(), end=".") # Prints the last word from the last position to the end