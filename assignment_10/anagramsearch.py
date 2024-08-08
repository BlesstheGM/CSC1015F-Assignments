# program to find anagrams of words
# Blessing Hlongwane
# HLNBLE002
# 03 May 2023

print("***** Anagram Finder *****")
import os.path
anagrams = []

try:
    my_file = open("EnglishWords.txt", "r")
    content = my_file.read().split()  # Making a list of every word
    my_file.close()
    user_input = input("Enter a word:\n")
    for word in content: # Checking everyword in the opened file
        if sorted(word) == sorted(user_input) and word!=user_input: # Finds Anagram
            anagrams.append(word) # Adds anagram into our list
    if anagrams == []:
        print("Sorry, anagrams of '{}' could not be found.".format(user_input))
    else:
        anagrams.sort()
        print(anagrams)
except:
    print("Sorry, could not find file 'EnglishWords.txt'.")