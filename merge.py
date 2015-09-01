# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:50:41 2015

@author: SSunshine
"""
"""
Merge function for 2048 game.
"""

def merge(row):
    
    # create list of nonzero elements
    #raw_num = [x for x in row if x]
    raw_num = filter(None, row) #optimized (thanks, Paul!)
    
    #create empty list for final row
    final_row = []
    
    if len(raw_num) == 1: # if row has only one element, no way to combine
        final_row = raw_num
    else:
        i = 0    
        while (i+1) < len(raw_num): # iterate through the nonzero elements
            if raw_num[i] == raw_num[i+1]: # if the element matches the one to its immediate right
                final_row.append(raw_num[i]*2) #double it and add it to the list
                i += 2 #skip the next raw_num element since it's already been combined
            else:
                final_row.append(raw_num[i]) # if element is not start of a pair, add it alone
                i += 1
        if i+1 == len(raw_num): # if last two elements weren't a pair and the index landed on single
            final_row.append(raw_num[-1]) #add that final single
        
    
    # we need to add some zeros on the end if the final row is shorter than the original row 
    len_diff = len(row) - len(final_row)
    if len_diff > 0: 
        final_row.extend([0]*len_diff)
            
    return final_row
            
    