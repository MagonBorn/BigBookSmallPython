"""Dice Math, by AL Sweugart al@inventwithpython.com
A flash card addition game where you sum the total on random dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, math
Reproduced here by: Matthew Mason"""
import random, time

# Set up the constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 70
CANVAS_HEIGHT = 24 - 3 # -3 for room to enter the sum at the bottom.

# The duration is in seconds:
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

# Points for correct/incorrect answers
REWARD = 4
PENALTY = 1

# The program hangs if all the dice can't fit on the screen
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
       '| O     |',
       '|       |',
       '|     O |',
       '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math, reproduced by Matthew Mason

Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each 
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))

# Keep track of correct/incorrect answers
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
print(startTime)
print(startTime + QUIZ_DURATION)

# # Main game loop
while time.time() < startTime + QUIZ_DURATION:
  sumAnswer = 0
  diceFaces = []
  for i in range(random.randint(MIN_DICE, MAX_DICE)):
    die = random.choice(ALL_DICE)
    diceFaces.append(die[0])
    sumAnswer += die[1]
  topLeftDiceCorners = []

  # Determin dice position
  for i in range(len(diceFaces)):
    while True:
      left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
      top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)
      
      # Get the x,y coordinates for all four corners
      topLeftX = left
      topLeftY = top
      topRightX = left + DICE_WIDTH
      topRightY = top
      bottomLeftX = left
      bottomLeftY = top + DICE_HEIGHT
      bottomRightX = left + DICE_WIDTH
      bottomRightY = top + DICE_HEIGHT

      # Check if this die overlaps with previous dice.
      overlaps = False
      for prevDieLeft, prevDieTop in topLeftDiceCorners:
        prevDieRight = prevDieLeft + DICE_WIDTH
        prevDieBottom = prevDieTop + DICE_HEIGHT
        for cornerX, cornerY in ((topLeftX, topLeftY),
                                 (topRightX, topRightY),
                                 (bottomLeftX, bottomLeftY),
                                 (bottomRightX, bottomRightY)):
          if (prevDieLeft <= cornerX < prevDieRight and prevDieTop <= cornerY < prevDieBottom):
            overlaps = True
      if not overlaps:
        topLeftDiceCorners.append((left, top))
        break
  
  # Draw dice on the canvas
  canvas = {}
  for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
    dieFace = diceFaces[i]
    for dx in range(DICE_WIDTH):
      for dy in range(DICE_HEIGHT):
        canvasX = dieLeft + dx
        canvasY = dieTop + dy
        canvas[(canvasX, canvasY)] = dieFace[dy][dx]
  
  for cy in range(CANVAS_HEIGHT):
    for cx in range(CANVAS_WIDTH):
      print(canvas.get((cx, cy), ' '), end='')
    print()
  
  response = input('Enter the su,: ').strip()
  if response.isdecimal() and int(response) == sumAnswer:
    correctAnswers += 1
  else:
    print('Incorrect, the answer is', sumAnswer)
    time.sleep(2)
    incorrectAnswers += 1

# Display the final score
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct: ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score: ', score)