# -*- coding: utf-8 -*-
"""
This program will print out numbers within a given range. If the number is 
divisible by number1 (3), the program will instead print out Crackle. If it is
divisible by number2 (5), it will print out Pop instead of the number. If the 
number is divisible by both number1 and number2, it will print out CracklePop.

The program will default to a range of 1 through 100 (inclusive).

@author: SSunshine
"""


def crackle_pop(start=1, end=100): 
    # Define the values of number1 and 2
    number1, number2 = 3, 5  

    # Generate the inclusive range of values the program needs to evaluate        
    for i in range(start, end+1):
         #If the value is divisible by both numbers, print CracklePop
        if i % (number1 * number2) == 0:
            print 'CracklePop'
        #If the value is divisible by number1, print Crackle 
        elif i % number1 == 0:
            print "Crackle"
        #If the value is divisible by number2, print Pop. 
        elif i % number2 == 0:
            print "Pop"
        # If the value is not divisible by either number, just print it 
        else:
            print i