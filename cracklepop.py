# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 13:54:37 2016

@author: SSunshine
"""


def crackle_pop(start, end, step=1): 
    number1 = 3
    number2 = 5    
    
    if step == 1:
        for i in range(start, end+step):
             #If the number is divisible by both 3 and 5, print CracklePop
            if i % (number1 * number2) == 0:
                print 'CracklePop'
            #If the number is divisible by 3, print Crackle 
            elif i % number1 == 0:
                print "Crackle"
            #If it's divisible by 5, print Pop. 
            elif i % number2 == 0:
                print "Pop"
            else:
                print i

    else:    
        i = start   
        while i < (end + 1):
            #If the number is divisible by both 3 and 5, print CracklePop
            if i % (number1 * number2) == 0:
                print 'CracklePop'
            #If the number is divisible by 3, print Crackle 
            elif i % number1 == 0:
                print "Crackle"
            #If it's divisible by 5, print Pop. 
            elif i % number2 == 0:
                print "Pop"
            else:
                print i
            i += step