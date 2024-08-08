# 
# Blessing Hlongwane
# HLNBLE002
# 18 March 2023W

import math

start = eval(input("Enter the start point M: "))
stop = eval(input("Enter the end point N: "))


for i in range(start , stop + 1):
    if stop - start != 0:
        b = str(i)
        if b == b[::-1]:
            if (math.sqrt(i) // 1) ** 2 == i:
                print(b)
    else:
        print("There are no palindrome perfect squares between", starz ,"and", )
        break