# program to find anagrams of words with the same length
# Blessing Hlongwane
# HLNBLE002
# 03 May 2023

my_file = open("EnglishWords.txt", "r")
content = my_file.read().split()
my_file.close()
print("***** Anagram Set Search *****")
length = eval(input("Enter word length:\n"))
anagrams = []
for word in sorted(content): 
    if len(word) == length: # Finds words with the length chosen
        anagrams.append(word) # Adds the words in a list
    else:
        pass
print("Searching...")
other_file = input("Enter file name:\n")



lists = []
index = 0
dicti = {}



print("Writing results...")

for word in sorted(anagrams): 
    dicti[word] = [] 
    # Finds anagrams in our list
    for b in anagrams[index+1:]:
        if (sorted(word) == sorted(b)) and ( word!=b ):
            dicti[word].append(b) # Dictionary where the key is the main word and and the values are the anagrams
    index += 1
    
new_file = open(other_file, "w")
new_file.close()
new_file = open(other_file, "a")
    
values = []

for key in dicti.keys():
    if dicti[key] != []: # If the key has anagrams
        if dicti[key][0] in values:
            pass
        else:
            dicti[key].insert(0, key) # Creating our new list
            values += dicti[key]
            print(dicti[key], file = new_file)

new_file.close()