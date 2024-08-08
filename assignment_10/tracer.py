# program to insert the docstring """DEBUG""" at the start of the file
# Blessing Hlongwane
# HLNBLE002
# 12 May 2023

import os.path

print("***** Program Trace Utility *****")
name = input("Enter the name of the program file: ")

myfile =[]
recent_file = open(name, "r")

for lines in recent_file: 
    myfile.append(lines) # Creating a list with lines in our file
    
recent_file.close()

bug = "BUG"

if bug in myfile[0]:  # If the word "Debug" is in our list
    print("Program contains trace statements")
    print("Removing...Done")
    new = open(name, "w")
    for lines in myfile: 
        if bug not in lines:
            new.write(lines) # Rewriting our file without the bug
    new.close()
else:
    print("Inserting...Done")
    new = open(name, "w")
    new.write("\"\"\"DEBUG\"\"\"\n") # Write "Debug" at the start of the file
    for lines in myfile:
        newline = lines.split()
        if "def" in newline: # Looking for our functions
            new.write(lines)
            other = newline[1]
            end = other.find("(") 
            new.write("    \"\"\"DEBUG\"\"\";print(\'"+other[:end]+"\')"+"\n")
        else:
            new.write(lines)
        
    new.close()   

