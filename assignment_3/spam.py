# Program to write a spam message
# Blessing Hlongwane
# HLNBLE002
# 24 February 2023

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money_in_usd = eval(input("Enter sum of money in USD:\n"))
final_amount = money_in_usd * 0.3 # Calculate 30% of the money
country_name = input("Enter country name:\n")

print("\nDearest", first_name, end="\n")
print("It is with a heavy heart that I inform you of the death of my father,",end="\n")
print("General Fayk", last_name, end=", ") 
print("your long lost relative from Mapsfostol", end=".\n")
print("My father left the sum of", money_in_usd, end="USD ") 
print("for us, your distant cousins.", end="\n")
print("Unfortunately, we cannot access the money as it is in a bank in", country_name, end=".\n")
print("I desperately need your assistance to access this money.", end="\n")
print("I will even pay you generously, 30% of the amount -", final_amount, end="USD,\n")
print("for your help.  Please get in touch with me at this email address asap.", end="\n")
print("Yours sincerely")
print("Frank", last_name)