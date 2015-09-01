# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 16:05:21 2015

@author: SSunshine
"""

import requests
import random
import numpy

#global variables 
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
#this isn't a perfect solution since many of these words are weird/uncommon
response = requests.get(word_site)
WORDS = response.content.splitlines()

def new_game():
    global word, tracker, guesses
            
    again = True
    while again:
        word = random.choice(WORDS)
        if not word[0].isupper(): # check if word is proper noun; if so, pick again
            again = False

    tracker = np.zeros(len(word))
    guesses = 0

class Blank:
     # definition of intializer
    def __init__(self, let, solv, pos):
        self.letter = let
        self.solved = solv
        self.position = pos
        
    # definition of getter for number
    def get_letter(self):
        return self.letter
    
    # check whether tile is exposed
    def is_solved(self):
        return self.solved

def draw():
    
    
blank_cntr = 0
while blank_cntr < len(word):
    print '_', 
    blank_cntr += 1

print ""
done = False

tries = 0

while not done:
    ltr = raw_input('Guess a letter: ')
    # way to improve game would be option to guess whole word at any time a la Wheel of Fortune
    print word
    print ltr
    done = True
    ltr_cntr = -1
    for c in word:
        ltr_cntr += 1
        if c = ltr:

def convert_letters_to_numbers(inputted):
    output = []
    for c in inputted:
        number = ord(character) - 96
        output.append(number)
    return output

def convert_numbers_to_letters(inputted):
    
            
        