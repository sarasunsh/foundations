# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 15:18:20 2015
@author: SSunshine
"""

#action items:
# - stuck in an infinite loop
# - write restart function to reduce code duplication
# - check that user input is only one letter / not any other input type
# - don't bother checking letters that have already been matched
# - doesn't count if you guess a letter you've already gotten

import requests
import random
import numpy

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
#this isn't a perfect source since many of these words are weird/uncommon
response = requests.get(word_site)
WORDS = response.content.splitlines() # produces list of words
guess_num = 10 # can set number of guesses allotted

def new_game():
    global word, tracker, guesses, done
    
    print 'Welcome to Sunshine Hangman!'    
    guesses = 0
    done = False        
    again = True
    while again:
        word = random.choice(WORDS)
        if not word[0].isupper(): # check if word is proper noun; if so, pick again
            again = False

    tracker = [0] * len(word)

    blank_cntr = 0
    while blank_cntr < len(word):
        print '_', 
        blank_cntr += 1
    print ""

new_game()
print word

while not done:
    # if they've exceeded allotted guesses, end the game & give restart option
    if guesses > guess_num - 1:
        print "You got hung!"
        print ""
        print "Would you like to try again?"
        restart = raw_input("If so, enter Y. Otherwise, enter any other key: ")
        if restart == 'Y':
            new_game()
            print word
        else:
            done = True
    # if gameplay is still ongoing...
    else:
        print tracker        
        ltr = raw_input('Guess a letter: ')
        # way to improve game would be option to guess whole word at any time a la Wheel of Fortune
        guesses += 1 # i want to move this but am not sure where yet
        c_cntr = -1 
        for c in word: # this isn't elegant, because it indexes letters that have already been solved
            c_cntr += 1 
            if c == ltr: 
                tracker[c_cntr] = ltr

        # draw the hangman board        
        b_cntr = -1        
        for b in tracker:
            b_cntr += 1
            if b == 0:
                print "_",
            else:
                print tracker[b_cntr],
        
        #check if all the blanks have been filled in        
        if 0 not in tracker:
            print "You got the word!"
            print ""
            print "Would you like to try again?"
            restart = raw_input("If so, enter Y. Otherwise, enter any other key: ")
            if restart == 'Y':
                new_game()
                print word
            else:
                done = True


#def convert_letters_to_numbers(inputted):
#    output = []
#    for c in inputted:
#        number = ord(character) - 96
#        output.append(number)
#    return output
#
#def convert_numbers_to_letters(inputted):
    
            
        