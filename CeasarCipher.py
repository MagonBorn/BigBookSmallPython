try:
  import pyperclip # pyperclip copies text to the clipboard
except:
  pass # If pyperclip is not installed, do nothing. It's no big deal

# Every possible symbol that can be encrypted/decrypted
# (!) You can add numbers and puncutation marks to encrypt those
# symbols as well
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# SYMBOLS = 'ABC'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
while True: # Keep asking until the user enters e or d
  print('Do you want to (e)ncrypt or (d)ecrypt?')
  response = input('> ').lower()
  if response.startswith('e'):
    mode = 'encrypt'
    break
  elif response.startswith('d'):
    mode = 'decrypt'
    break
  else:
    print('please enter the letter e or d')
  
# Let the user enter the key to use
while True: # Keep asking until the user enters a valid key
  maxKey = len(SYMBOLS) - 1
  print('Please enter the key (0 to {}) to use'.format(maxKey))
  response = input('> ').upper()
  if not response.isdecimal():
    continue
  if 0 <= int(response) < len(SYMBOLS):
    key = int(response)
    break

# Let the user enter the message to encrypt
print('Enter the message to {}'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters:
message = message.upper()

# Stores the encrypted/decrypted message form of the message
translated = ''

# Encrypt/Decrypt each symbol in the message
for symbol in message:
  if symbol in SYMBOLS:
    # Get the encrypted (or decrypted) number for this symbol
    num = SYMBOLS.find(symbol) # Get the number of the symbol
    if mode == 'encrypt':
      num = num + key
    elif mode == 'decrypt':
      num = num - key
    
    # Hanbdle the wrap-around if num is larger then the length of
    # SYMBOLS or less than 0
    if num >= len(SYMBOLS):
      num = num - len(SYMBOLS)
    elif num < 0:
      num = num + len(SYMBOLS)
    
    # Add encrypted/decrypted number's symbols to translated
    translated = translated + SYMBOLS[num]
    # translated = translated + symbol
  else:
    # Just add the symbol without encrypting/decrypting
    translated = translated + symbol

# Print the encrypted/decrypted string to the screen:
print(translated)

try:
  pyperclip.copy(translated)
  print('Full {}ed text copied to clipboard.'.format(mode))
except:
  pass # Do nothing if pyperclip wasn't installed

# Exploring the program

# Q.1: What happens if you change SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' to SYMBOLS = 'ABC'?
# A.1: The only letter that will change are A, B, and C, all other letters will be printed as they entered: e.g., with a key of 1, 'bye' becomes 'cye'

# Q.2: What happens when you encrypt a message with a key 0?
# A.2: The encrypted message remains exactly the same

# Q.3: What error message do you get if you delete or comming out translated = ''?
# A.3: The program produces a runtime NameError as it's trying to assign letters to a variable that hasn't been defined.

# Q.4: What error message do you get if you delete or comment out key = int(response)?
# A.4: Same as before, a NameError occurs as key is not defined before trying to be assigned to.

# Q.5: What happens if you change translated = translated + SYMBOLS[num] to translated = translated + symbol?
# A.5: The current letter being iterated over is added to the 'translated' variabler rather than the
# character at the 'SYMBOLS' variable index.