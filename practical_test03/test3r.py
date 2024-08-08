# CSC1015F Practical Test: Version R
# Given an input string of numbers, find all combinations of
# numbers that can be formed using digits in the same order.

# Your name here
# Your student number here
# 15 May 2023

def printCombinations(input_digit, index, output, outLength):
    if index + 1 == len(input_digit):
        pass
    else:
        output[index+1] = input_digit[index] +  ""*outLength + input_digit[index+1] + ""*outLength + input_digit[index+2] 
        return output[index] + printCombinations(input_digit, index+1, output[index+1], outLength+1)
    # Your code here
    


# Driver code
def main():
    input_digit = input('Enter a string of digits:\n')
    output = [0] * 100

    # initialize output with empty string
    output[0] = '\0'

    print('Possible combinations that can be made using', input_digit, 'are:')
    printCombinations(input_digit, 0, output, 0)


if __name__ == '__main__':
    main()
