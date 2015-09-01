# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 13:37:48 2015

@author: SSunshine
"""

# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
prompt = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank): # create Card object      
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):  # return a string representation of a card       
        return self.suit + self.rank

    def get_suit(self): # return card suit
        return self.suit

    def get_rank(self): # return card rank
        return self.rank

    def draw(self, canvas, pos): # draw card face up
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
   
# define hand class
class Hand:
    def __init__(self): # create Hand object      
        self.cards = []
        self.value = 0

    def __str__(self): # return a string representation of a hand        
        if len(self.cards) == 0:
            return "This hand is empty."
        else:
            s = "The following cards are in this hand:"
            for card in self.cards:
                s += " "+str(card)
            return s

    def add_card(self, card):  # add a card object to a hand
        self.cards.append(card)

    def get_value(self): # return value of hand
        aces = 0
        self.value = 0
        for card in self.cards:
            self.value += VALUES.get(card.rank)
            if card.rank == 'A':
                aces +=1
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        if self.value <12 and aces > 0:
            self.value +=10     
        return self.value      
   
    def draw(self, canvas, y_adj,  hide):   # draw hand
        i = 0
        for card in self.cards:
            card.draw(canvas, [100 + i*CARD_SIZE[0], 300 + 100*y_adj])
            i += 1
        if hide:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                               [100 + CARD_BACK_CENTER[0], 300 + 100*y_adj + CARD_BACK_CENTER[1]] , CARD_BACK_SIZE)
        
       
# define deck class 
class Deck:
    def __init__(self): # create a Deck object  
        self.deck = []
        [[self.deck.append(Card(j, i)) for j in SUITS] for i in RANKS]
        
    def shuffle(self): # shuffle the deck     
        random.shuffle(self.deck)

    def deal_card(self): # deal a card object from the deck    
        dealt = self.deck[0]
        self.deck.remove(dealt)
        return dealt
    
    def __str__(self): # return a string representing the deck       
        s = "Deck:"
        for card in self.deck:
            s += " "+str(card)
        return s

#define event handlers for buttons
def deal():
    global prompt, outcome, in_play, d, player, dealer, score
    if in_play:
        score -= 1
    else:
        in_play = True 
    d = Deck()
    player = Hand()
    dealer = Hand()
    d.shuffle()
    player.add_card(d.deal_card())
    player.add_card(d.deal_card())
    dealer.add_card(d.deal_card())
    dealer.add_card(d.deal_card())   
    prompt = "Hit or stand?"
    outcome = ""
    
def hit():
    global in_play, score, outcome, prompt
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(d.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome = "You have busted."
            in_play = False
            score -= 1      
            prompt = "New deal?"
        
def stand():
    global in_play, score, outcome, prompt
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while in_play:
        if dealer.get_value()< 17:
            dealer.add_card(d.deal_card())
        else: # assign a message to outcome, update in_play and score
            in_play = False
            if dealer.get_value() > 21:
                outcome = "Dealer busts."
                score += 1             
            elif dealer.get_value() < player.get_value():
                outcome = "Player wins!"
                score += 1
            else:
                outcome = "Dealer wins."
                score -= 1
            prompt = "New deal?"
                
# draw handler    
def draw(canvas):
    dealer.draw(canvas, -1, in_play)
    player.draw(canvas, 1, False)
    canvas.draw_text(prompt, [100,150], 30, "white", "sans-serif")
    canvas.draw_text("Haus von Zunszajn: Blackjack", [200,20], 15, "yellow", "sans-serif")
    canvas.draw_text(outcome, [100,100], 30, "white", "sans-serif")
    canvas.draw_text("Score: "+str(score), [10,550], 20, "blue", "sans-serif")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
