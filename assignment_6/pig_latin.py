# program to output sentence in pig latin
# Blessing Hlongwane
# HLNBLE002
# 23 March 2023

sentence = input("Enter a sentence:\n") + " "
start = 0
vowel = "oeaiu"
count = 0
for space in sentence:
    if space == " ":
        count = 0
        position = sentence[start:].find(space) # Finds position of space character
        last_position = position + start # last position is the sum of the space character and start position
        word = sentence[start:last_position].lower()
        first_letter = sentence[start:last_position][0]    # First letter of a string after space or before a string    
        
        # Identifies whether the first letter is a vowel
        if first_letter in vowel:
            print("{0}way".format(word), end=" ")
        else:
            # Searches for a vowel in every letter of a word if the first character is not a vowel
            for letter in word:
                    if count == 0:
                        if letter in vowel:
                            vowel_in_sentence = word.find(letter)
                            print(word[vowel_in_sentence::] + "a" + word[:vowel_in_sentence] + "ay", end=" ")
                            count += 1
                            break
                    else:
                        pass
        start += position + 1