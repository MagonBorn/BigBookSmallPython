import random
import sys

# Set up the constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com
        
  Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    The dealer stops hitting at 17. ''')

    money = 5000
    while True:  # Main game loop.
        # Check if the player has run out of money
        if money <= 0:
            print('You\'re broke!')
            print('Good thing you weren\'t playing with real money.')
            print('Thanks for playing!')
            sys.exit()

        # Let the player enter their bet for this round:
        print('Money: ', money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions
        print('Bet:', bet)
        while True:  # Keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if player has bust
            if getHandValue(playerHand) > 21:
                break
            
            # Get the player's move, either H, S, or D:
            move = getMove(playerHand, money - bet)

            # Handle the player actions:
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)
            if move in ('H', 'D'):
                # Hit/Doubleing down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has bust
                    continue
            if move in ('S', 'D'):
                # Stand/Doubling down stops the player's turn
                break
        
        # Handle the dealers actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits
                print('Dealer Hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # The dealer has bust
                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost or tied:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')
        input('Press Enter to continue...')
        print('\n\n')


# --------- Game Functions ----------
# Return the amount the player wants to bet
def getBet(maxBet):
    # Ask the player how much money they want this round.
    while True:  # Keep asking until they enter a valid amount
        print('How much do you bet? (1-{} or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue  # If the player didn't enter a number, ask again
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet

# Return a shuffled deck of cards


def getDeck():
    # Return a list of (rank, suit) tuples for all 52 cards.
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck

# prints the players and dealers current hand


def displayHands(playerHand, dealerHand, showDealerHand):
    '''Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False'''
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])
    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

# Returns the value of the hand passed in


def getHandValue(cards):
    '''Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value).'''
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]  # Card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # Face cards are worth 10 points
            value += 10
        else:
            value += int(rank)

    # Add the value for the aces:
    value += numberOfAces  # Add 1 per ace
    for i in range(numberOfAces):
        # If another 10 can be added without busted, do so:
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    # Display all the cards in the cards list.
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card
        if card == BACKSIDE:
            # Print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    # Print each row on the screen
    for row in rows:
        print(row)

def getMove(playerHand, money):
    '''Ask the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down.'''
    while True: # Keep looking until the player enters a correct move
        # Determine what moves the player can make
        moves = ['(H)it', '(S)tand']
        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        
        # Get the player's move:
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move # Player has entered a valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move # Player has made a valid move
if __name__ == '__main__':
    main()

# Exploring the program

# Q.1: How can you make the player start with a different amount of money?
# A.1: Update the money vairable on line 26 to whatever value you want

# Q.2: How does the program prevent the player from betting more money than they have?
# A.2: On line 124, the program checks that the value entered by the player (after a number of other checks), is less than the amount of money the player currently has and greather than one.

# Q.3: How does the program represent a single card?
# A.3: Each card is represented as a tuple consisting of a rank and a suit such as "7 of hearts". The program contains a function that visually represents the cards as ascii art in the console.

# Q.4: How does the program represent a hand of cards?
# A.4: A hand of cards is a list of 2 or more single cards that has been popped from an individual deck of cards for both the payer and the dealer.

# Q.5: What do each of the strings in the rows list (created on line 188) represent?
# A.4: Each string in the rows list represents an individual row when building the ascii image of a card as below:
# 1  ___   ___   ___
# 2 | 6 | |3  | |K  |
# 3 | ♠ | | ♠ | | ♥ |
# 4 |__6| |__3| |__K|
# 5

# Q.6: What happens if you delete or comment out random.shuffle(deck) on line 138?
# A.6: The deck will always be in the reverse order in which its created meaning the first cards pulled will always be Ace of Clubs, then King of Clubs, then Queen of Clubs, then Jack of Clubs, then 10 of Clubs, etc... The player will always lose.

# Q.7: What happens if you change money -= bet on line 101 to money += bet?
# A.7: You would add to your total money rather than take it away

# Q.8: What happens when showDealerHand in the displayHands() function is set to True? What happens when it is False?
# A.8: True reveals the dealers first card and draws it face up on the console. False will draw the card face down so its value cannot be seen.