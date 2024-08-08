# 
# Blessing Hlongwane
# HLNBLE002
# 09 March 2023

number  = eval(input("""Enter the start number:  
"""))

if -6 < number <2:
        for b in range(number, number + 7, 1):
                if len(str(b)) < 2:
                        print(" ", b, end="")
                else:
                        print("", b, end="")
        print("")
        for c in range(number + 7, number + 14):
                if len(str(c)) < 2:
                        print(" ", c, end="")  
                else:
                        print("", c, end="")
        print("")
        for d in range(number + 14 , number + 21):
                        print("", d , end="")
        print("")
        for e in range(number + 21, number + 28):
                print("", e , end="")
        print("")
        for f in range(number + 28, number + 35):
                print("", f , end="")
        print("")
        for g in range(number + 35, number + 42):
                print("", g , end="")        