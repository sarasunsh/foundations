# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 14:38:18 2015

@author: SSunshine
"""


#Lesson 1: Guess the Number
#
#Write a program that will first randomly generate a number unknown to the user. 
#The user needs to guess what that number is. (In other words, the user needs to 
#be able to input information.) If the user’s guess is wrong, the program should 
#return some sort of indication as to how wrong (e.g. The number is too high or 
#too low). If the user guesses correctly, a positive indication should appear. 
#You’ll need functions to check if the user input is an actual number, to see 
#the difference between the inputted number and the randomly generated numbers, 
#and to then compare the numbers.
#
#Concepts to keep in mind:
#    Random function
#    Variables (global and local)
#    Integers
#    Input/Output (and input sanitization)
#    Print
#    While loops
#    If/Else statements

import random

upper_bound = 100
lower_bound = 1

magic_num = random.randint(lower_bound, upper_bound) 
# can play with having bounds set by user 

guessed = False

while not guessed:
    guess = input('Guess the number:')
    if guess > magic_num:
        print "Too high! Try again."
    elif guess < magic_num:
        print "Too low! Try again."
    else:
        print "Congrats! You nailed it. That's not all you're gonna nail tonight ;)"
        guessed = True

