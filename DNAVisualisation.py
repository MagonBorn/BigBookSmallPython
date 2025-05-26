import random
import sys
import time

pause = 0.15

# These are the individual rows of the DNA animation:
rows = [
  '         ##',
  '        #{}-{}#',
  '       #{}---{}#',
  '      #{}-----{}#',
  '     #{}------{}#',
  '    #{}------{}#',
  '    #{}-----{}#',
  '     #{}---{}#',
  '     #{}-{}#',
  '      ##',
  '     #{}-{}#',
  '     #{}---{}#',
  '    #{}-----{}#',
  '    #{}------{}#',
  '     #{}------{}#',
  '      #{}-----{}#',
  '       #{}---{}#',
  '        #{}-{}#'
]

try:
  print('DNA ANimation')
  print('Press Ctrl-C to quit...')
  time.sleep(2)
  rowIndex = 0

  while True:
    rowIndex += 1
    if rowIndex == len(rows):
      rowIndex = 0
    
    if rowIndex == 0 or rowIndex == 9:
      print(rows[rowIndex])
      continue

    randomSelection = random.randint(1, 4)
    match randomSelection:
      case 1:
        leftNucleotide, rightNucleotide = 'A', 'T'
      case 2:
        leftNucleotide, rightNucleotide = 'T', 'A'
      case 3:
        leftNucleotide, rightNucleotide = 'C', 'G'
      case 4:
        leftNucleotide, rightNucleotide = 'G', 'C'
    
    print(rows[rowIndex].format(leftNucleotide, rightNucleotide))
    time.sleep(pause)
except KeyboardInterrupt:
  sys.exit()