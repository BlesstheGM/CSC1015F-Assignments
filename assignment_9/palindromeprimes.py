# program to print palindrome prime numbers
# Blessing Hlongwane
# HLNBLE002
# 27 April 2023

import sys
sys.setrecursionlimit (30000)

begin = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

# Below function checks whether a number is a prime number
def prime(our_number, factors=2):
    if our_number == factors:
        return True
    elif our_number % factors == 0:
        return False
    return prime(our_number, factors + 1)  
        
        
va = []
    
# Returns numbers from the given range   
def ret(number, maxi):  
    if maxi + 1 != number:
        va.append(maxi)
        return ret(number , maxi-1)
ret(begin, end)
index = 0
    
length_of_list = len(va)
va.reverse()

def pali():
    global length_of_list
    global index
    global number
    character = str(va[index])
    if length_of_list == index + 1 : # Chech if palindrome on last character
        if prime(va[index]) == True:
            print(character)
    else:
        if character == character[::-1]: # Check If Palindrome
            if prime(va[index]) == True:
                print(character)
            index += 1
            return pali()
        elif character != character[::-1]:
            index += 1
            return pali()        
        

pali()