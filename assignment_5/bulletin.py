# program to simulate a BBS
# Blessing Hlongwane
# HLNBLE002
# 15 March 2023

text_forty_2 = "The meaning of life is blah blah blah ..."
text_ten_fifteen = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
message = "no message yet"

while True:
    # Always show these options
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    selection = input("Enter your selection:\n")
    # What happens for each user input
    if selection.upper() == "L":
        print("List of files: 42.txt, 1015.txt")
    elif selection.upper() == "D":
        file_name = input("Enter the filename:\n")
        if file_name == "1015.txt": 
            print(text_ten_fifteen)
        elif file_name == "42.txt":
            print(text_forty_2)
        else:
            print("File not found")
    elif selection.upper() == "X":
        print("Goodbye!")
        break
    elif selection.upper() == "E":
        message = input("Enter the message:\n")
    elif selection.upper() == "V":
        print("The message is:", message)