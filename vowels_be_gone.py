# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

text = ""
#vowels = {"a", "e", "i", "o", "u"}
notVowels = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}
output= [] 

while text != "quit":
    text = input("Please type a string of text: ").lower()
    for letter in text: 
        if letter in notVowels:
            output += letter
    print(sorted(output))
    
