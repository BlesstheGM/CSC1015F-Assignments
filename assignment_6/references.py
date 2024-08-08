# program to reformat references
# Blessing Hlongwane
# HLNBLE002
# 23 March 2023

reference = input("Enter the reference: \n")

second_bracket = reference.find(")") # Finding the position of the second bracket
coma = reference[second_bracket+2:].find(",") # Finding a coma
print("Reformatted reference:")
print(reference[:second_bracket+1].title(), end = " ") # Print words before the second bracket
print(reference[second_bracket+2:coma+second_bracket+3].capitalize() , end= " ")  # Print from the second + 2 upto the coma then capitalize
print(reference[coma+second_bracket+4:], end=" ") # Print words after the coma to the last letter of the sentence