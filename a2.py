# Import necessary modules
import time
import random

# Define the ranks and suits

ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards

deck = [(suit, rank) for suit in suits for rank in ranks]

# Shuffle the deck 

random.shuffle(deck)


deck1 = deck[:len(deck)//2]
deck2 = deck[len(deck)//2:]

def card_comparison(p1_card, p2_card):
    if ranks.index(p1_card[1]) > ranks.index(p2_card[1]):
        return 1
    elif ranks.index(p1_card[1]) < ranks.index(p2_card[1]):
        return 2
    else:
        return 0

def play_round(player1_hand, player2_hand):
    #pick out the cards to be played

    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    print(f"Player 1 plays {p1_card}, Player 2 plays {p2_card}")

    #compare the cards to determine the winner based on cards rank

    result = card_comparison(p1_card, p2_card)

    if result == 1:

        print("Player 1 wins the round")
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)

    elif result == 2:
        print("Player 2 wins the round")
        player2_hand.append(p1_card)
        player2_hand.append(p2_card)

    else:
        print("Peace!") #if there is a tie
        peace(player1_hand,player2_hand)
        
        
def peace(player1_hand, player2_hand):
    #ensure both players have enough cards to proceed with a peace
    if len(player1_hand) < 4:
        print("Player 1 does not have enough card for peace! Player 2 wins the game!")
        player2_hand.append(player1_hand) #player 2 gets all remaining cards
        player1_hand.clear()
        return

    elif len(player2_hand) < 4:
        print("Player 2 does not have enough card for peace! Player 1 wins the game!")
        player1_hand.append(player1_hand) #player 1 gets all remaining cards
        player2_hand.clear()
        return

     # take 3 card face down and 1 card face up from both players
    while len(player1_hand) > 4  and len(player2_hand) > 4:
        p1_war_cards = [player1_hand.pop(0) for _ in range(4)] #3 cards + 1 for comparison
        p2_war_cards = [player2_hand.pop(0) for _ in range(4)]

        print(f"Player 1 put down {p1_war_cards[:-1]} and reveal {p1_war_cards[-1]}")
        print(f"Player 2 put down {p2_war_cards[:-1]} and reveal {p2_war_cards[-1]}")

        #comparing the face up card

        result_peace = card_comparison(p1_war_cards[-1], p2_war_cards[-1])

        if result_peace == 1:
            print("Player 1 wins the war!")
            player1_hand.extend(p1_war_cards + p2_war_cards)
            return


        elif result_peace == 2:
            print("Player 2 wins the war!")
            player2_hand.extend(p1_war_cards + p2_war_cards)
            return
        else:
            print("Another tie! War continues!")
    
def game_loop(player1_hand, player2_hand):
    round_count = 0

    # the game runs as long as both players have cards

    while len(player1_hand) > 0 and len(player2_hand) > 0:
        round_count += 1
        play_round(player1_hand, player2_hand)
        time.sleep(0.2)

def play_game(player1_hand, player2_hand):
    game_loop(player1_hand, player2_hand)
    #determine the winner

    if len(player1_hand) == 0 :
        print("Player 2 wins the game!")
    else:
        print("Player 1 wins the game!")

# Calling the main function to start the game

play_game(deck1, deck2)
