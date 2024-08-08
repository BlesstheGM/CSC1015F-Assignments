# program to encrypt a message
# Blessing Hlongwane
# HLNBLE002
# 25 April 2023

start = 0
a = list(input("Enter a message:\n"))
b = ""

def change(a, start):
    global b
    if len(a) != start:
        if a[start] == 'z':
            b += 'a'
        elif a[start] == ' ': 
            b += ' '
        elif a[start] == '.':
            b += '.'
        else:
            b += chr(ord(a[start])+1)
        change(a, start+1)
    return b

print("Encrypted message:")

if ''.join(a).islower():
    print(change(a, start))
else:
    print(''.join(a))