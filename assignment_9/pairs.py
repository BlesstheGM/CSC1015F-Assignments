# program to count the number of consecutive pairs
# Blessing Hlongwane
# HLNBLE002
# 26 April 2023


message = input("Enter a message:\n")


def pairs(message):
    length = len(message) 
    if length == 1 or length == 0: # There are no pairs to check anymore
        return 0
    else:
        if message[0] == message[1]: #If the current letter is the same as the next letter
            return 1 + pairs(message[2:]) 
        else:
            return pairs(message[1:])
                
                
print("Number of pairs:", pairs(message))                