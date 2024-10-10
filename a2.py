# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

deck = [(suit, rank) for suit in suits for rank in ranks]
print(deck)

# Shuffle the deck 
random.shuffle (deck)
print(deck)

# Split the deck into two hands

deck_middle = int(len(deck) /2)
p1_hand = deck[:deck_middle]
p2_hand = deck [deck_middle:]

def card_comparison(p1_card, p2_card):
    p1_rank = ranks.index(p1_card[1])
    p2_rank = ranks.index(p2_card[1])

    if p1_rank > p2_rank:
       return 1
    elif p1_rank < p2_rank:
       return 2 
    else:
       return 0
 
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here


def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here

def play_game():
    """Main function to run the game."""
    # Your code here

# Call the main function to start the game
play_game()
