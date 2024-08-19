import datetime
import random
'''The birthday Paradox is a problem showcasing the suprisingly high probability
that two people will have the same birthday in a small group of people. This program
performs several probability experiments to determine the percentages for groups of
different sizes.'''

'''In a group as small as 23 people, there's a 50% chance of a matching birthday'''


def getBirthdays(numberOfBirthdays):
    # Returns a list of random date objects
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is uninportant for the simulation, however, all birthdays must have the same year
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    # Returns the date object of a birthday that occurs more than once in the birthday list
    if len(birthdays) == len(set(birthdays)):
        # All birthdays are unique, so return None. (Set can only contain unique elements)
        return None
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday


# Display the intro
print('''\nThe birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is suprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
      
(It's not actually a paradox, it's just a suprising result.)\n''')

while True:  # Kepp asking until the user enters a valid amount
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amount

# Set up a tuple of month names in order
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

# Generate the birthdays
print('\nHere are ', numBDays, ' birthdays: ', end='')
birthdays = getBirthdays(numBDays)

# Display the birthdays
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display the results
print('\nIn this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on ', dateText)
else:
    print('there are no matching birthdays.')

# Run through 100,000 simulations
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them
for i in range(100000):
    # Report on the progress of every 10,000 simulations
    if i % 1000 == 0:
        print(i, ' simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch/100000 * 100, 2)
print('''Out of 100,000 simulations of {} people there was a matching birthday
in that group {} times. This means that {} people have a {}% chance of having
a matching birthday in their group. That\'s probably more than you would think'''.format(
    numBDays, simMatch, numBDays, probability
))

# Exploring the program

# Q.1: How are the birthdays represented in this program?
# A.1: The birthdays are represented as a date objkect using the class datetime.date. It required three arguments that must be integers: year, month, day.

# Q.2: How could you remove the maximum limit of 100 birthdays the program generates?
# A.2: ON line 48, we can increase the number in the conditional statement from 100 to whatever other number we desire.

# Q.3: What error message do you get if you delete or comment out numBDays = int(response) on line 49?
# A.3: The program generates a "NameError: name 'numBDays' is not defined

# Q.4:How can you make the program display full month names, such as 'January' instead of 'Jan'?
# A.4: By updating the tuple variable MONTHS to include the full name of the month rather than the abbreviated version.

# Q.5: How could you make 'X simulations run...' Appread every 1,000 simulations instead of every 10,000?
# A.5: We can update the calculation on line 89 to 'i % 1000 == 0'.
