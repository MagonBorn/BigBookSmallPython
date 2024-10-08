import sys
import random
import time

try:
    import bext
except ImportError:
    print('''
        This program requires the bext module, which you can install
        by following the instructions at https://pypi.org/project/Bext/''')
    sys.exit()

# Set up the constants
WIDTH, HEIGHT =  bext.size() # returns a tuple of the (width, height) of the current terminal.
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.1
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    # Generate Logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4),
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS)
        })
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1 # Make sure X is even so logo can hit the corner
    
    # variables
    cornerBounces = 0

    # Main Program loop
    while True:
        # Handle each logo in the logos list
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]

            # See if the logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # See if logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            
            if logo[DIR] != originalDirection:
                # Change colour when the logo bounces
                logo[COLOR] = random.choice(COLORS)

            # Move the logo (X moves by 2 because the terminal characters are twice as tall as they are wide)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Display number of corner bounces
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner Bounces', cornerBounces, end = '')

        for logo in logos:
            # Draw the logos at their new location:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end = '')

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo')
        sys.exit()

# Exploring the program

# Q.1: What happens if you change WIDTH, HEIGHT = bext.size() to WIDTH, HEIGHT = 10, 5?
# A.1: In my terminal, the height is set to 5 but the width remains the length of the terminal and the DVD logos reach past the end causing the program to crash.

# Q.2: What happens if you replace DIR: random.choice(DIRECTIONS) with DIR: DOWN_RIGHT?
# A.2: All the logos start off with their movement set in the same direction: Down right

# Q.3: How can you make the corner counces text not appear on the screen?
# A.3: Remove or comment out the print statement on line 115

# Q.4: What error message do you get if you delete or comment out the cornerCounces = 0 on line 45?
# A.4: Unbound local Error: Cannot access local variable 'cornerBounces; where it is not associated with a value
