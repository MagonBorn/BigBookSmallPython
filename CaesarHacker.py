# Let the user specify the message to hack
print('Enter the encrypted Caesar cipher message to hack')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted:
# This must match the SYMBOLS used when encrypting the message.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop through every possible key
  translated = ''

  # Decrypt each symbol in the message
  for symbol in message:
    if symbol in SYMBOLS:
      num = SYMBOLS.find(symbol) # get the index of the symbol
      num = num - key # decrypt the message

      # Handle the wrap-around
      if num < 0:
        num = num + len(SYMBOLS)
      # Add decrypted number's symbol to translated
      translated = translated + SYMBOLS[num]
    else:
      # Just add the symbol without decrypting
      translated = translated + symbol
  # Display the key being tested, along with its decrypted text:
  print('Key #{}: {}'.format(key, translated))

  # Exploring the program

  # Q.1: What error message do you get if you delete or comment out translated = '' on line 10?
  # A.1: A NameError as the translated variable has not been defined.

  # Q.2: What happens if you change translated = translated + SYMBOLS[num] on line 22 to translated = translated + symbol?
  # A.2: The program simply return the message without doing any decryption

  # Q.3: What happens if you enter an unencrypted message into the Caesar cipher hacker program?
  # A.3: The program will produce evert possible encryption variant for the given message. 