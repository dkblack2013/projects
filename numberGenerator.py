#trying to create a random number generator + guessing game
import random
guess = 0
win = 0
trueNumber = random.randint(1,100)
print("I'm a computer, and I bet you can't guess the number I'm thinking of between 1 and 100!")
print('\n')
print("I'll give you five guesses.")
print('\n')
print(trueNumber)
#while win == 1:
for i in range(0,5):
    if guess != trueNumber:
        print('Please take a guess:')
        guess = input()
    elif guess == trueNumber:
        print("Wow, you actually guessed it! I'm impressed.")
        win = 1
        break


print("You couldn't figure it out...")
print("The number was " + str(trueNumber)+".")


