import sys

bitmap = '''
....................................................................
   ************** * *** ** * ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................'''

print('Bitmap Message Program')
print('Enter the message to display with the bitmap')

# Get user input
message = input('> ')
if message == '':
  sys.exit()

# Loop over each line in the bitmap (splitlines() returns a list of strings, breaking at line boundaries such as \n, \r, etc...)
for line in bitmap.splitlines():
  for i, bit in enumerate(line):
    if bit == ' ':
      print(' ', end = '')
    else:
      print(message[i % len(message)], end = '')
  print()

# Exploring the program

# Q.1: What happens if the player enters a blank string for the message?
# A.1: The program quits and stops running

# Q.2: Does it matter what the nonspace characters are in the bitmap variable's string?
# A.2: Yes, The program loops through each character in each line, if there is an empty space, the program will print and empty space, however if any other character is present, the program will replace it with the next sequential character of the input. for example: with a input message of hello, ** ***. becomes he lloh

# Q.3: What does the i variable on line 36 represent?
# A.3: The i represents the index of the current character being checked in each line.

# Q.4: What bug happens if you delete or comment out print() on line 41?
# A.4: All text output is on a single wrapped line. Because each print function in the loop uses the keyword argument end='', the print function in the proceeding loop continues to output text on the same line rather than on a new line. The print function at the end automatically adds a new line on each loop.