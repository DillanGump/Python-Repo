# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 10
answer = random.randint(1, highest)
#answer = 5

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer :
    print("Congrats, you got it first try. Please play again")
else :
    while guess != answer and guess != 0:
        print("\nSorry, you have not guessed correctly.")
        if guess > answer :
            print("Please guess lower")
        else :
            print("Please guess higher")
        guess = int(input())
        if guess == answer :
            print("\nCongrats, you guessed it")
    print("Thank you for playing. Goodbye.")

                
        
    
    
    
    
''''
    print("You got it first time")
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
'''
