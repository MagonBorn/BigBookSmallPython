"""Cho-Han, by Al Sweigart al@inventwithpython.com reproduced by Matthew Mason
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han by Al Sweigart al@inventwithpython.com reproduced by Matthew Mason
      
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 5000
while True:  # Main game loop
    print(
        'You have, {0} mon. How much do you want to bet? (or QUIT)'.format(purse))
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet')
        else:
            # This is a valid bet
            pot = int(pot)  # Convert pot to an integer
            break
    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks you for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Detemine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display bet results:
    if playerWon:
        print('You won! you take, {}, mon.'.format(pot))
        purse = purse + pot
        print('The house collects a', pot // 10, 'mon fee.')
        purse = purse - (pot//10)
    else:
        purse = purse - pot
        print('You Lost!')
    
    # Check if the player has run out of money
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playering!')
        sys.exit()

# Exporling the program

# Q.1: How can the player start with a different amount of money?
# A.1: By changing the amount of money assigned to the variable purse on line 19

# Q.2: How does the program prevent the player from betting more money than they have? 
# A.2: On line 30, the program checks that the bet entered is not more than the player current has in their purse

# Q.3: How doe sthe program know if the sum of the two dice is even or odd?
# A.3: By combining the values of each die and using the modulo operation to return the remainder of dividing the result by 2.
# This will give us the values or either 1 or 0 (Odd or Even). 0 = Even, 1 = Odd.

# Q.4: What happens if you change random.randint(1, 6) on line 37 to random.randint(1, 1)?
# A.4: The value of the first dice will always be 1

# Q.5: Does the house still collect a 10 percent fee if you change pot//10 on line 73 to 0?
# A.5: No the house does not take a percentage fee.

# Q.6: What happens if you delete or comment out lines 80, 81, 82, and 83? 
# A.6: When the players purse reaches 0 the game doesn't quit automatically. 