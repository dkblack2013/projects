#creating a random dice roll
import random
#create the dice function
def dice():
    # select the roll value
    roll = random.randint(1, 6)
    if roll == 1:
        print('---------')
        print('         ')
        print('    0    ')
        print('         ')
        print('---------')
    elif roll == 2:
        print('---------')
        print('  0      ')
        print('         ')
        print('      0  ')
        print('---------')
    elif roll == 3:
        print('---------')
        print('  0      ')
        print('    0    ')
        print('      0  ')
        print('---------')
    elif roll == 4:
        print('---------')
        print('  0   0  ')
        print('         ')
        print('  0   0  ')
        print('---------')
    elif roll == 5:
        print('---------')
        print('  0   0  ')
        print('    0    ')
        print('  0   0  ')
        print('---------')
    elif roll == 6:
        print('---------')
        print('  0   0  ')
        print('  0   0  ')
        print('  0   0  ')
        print('---------')
    else:
        print("The dice fell off the table. Please roll again.")
#setup the ability to roll multiple times
go = 'x'
while go != 'y':
    #roll the die
    dice()
    print('Press x to roll again.\nPress y to stop.')
    #input 'go' value to determine the next roll
    go = input()
print("Thank you for playing!")