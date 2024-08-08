# program to return integer and factorial
# Blessing Hlongwane
# HLNBLE002
# 12 April 2023

def get_integer(s):
   d = print("Enter ", s,":", sep="")
   my_digit = input("")
   while not my_digit.isdigit ():
      d = print("Enter ", s,":", sep="")
      my_digit = input("")
   my_digit = eval (my_digit)       
   return my_digit
    
def calc_factorial(my_digit):
    product = 1
    while my_digit > 0:
        product *= my_digit
        my_digit -= 1
    return product
    


