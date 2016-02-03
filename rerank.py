# -*- coding: utf-8 -*-
"""
Corrects the Physical Therapist's rankings on the survey so that 
if they ranked items with the same score, subsequent rankings 
are skipped (think US News & World Report)

Created on Wed Feb 03 15:02:56 2016

@author: SSunshine
"""

from collections import Counter
from copy import deepcopy
import csv

def redo_ranking(test):
    count = Counter()
    output = deepcopy(test)
   
    # Count how many times each ranking appears
    for item in test:
        count[item] += 1
        
    dicty = {}
    
    # Adjust the rankings to account for repeats
    track = 1
    for i in range(1, len(test)+1):
        dicty[i] = track
        track += count[i]

    # Rewrite rankings
    for j, k in enumerate(test):
        if type(k) == int: # Some cells have asterisk as an entry.
            output[j] = dicty[k]
        
    return output

def get_data(reader):
    
#    reader = csv.reader(open('data_file'))
    PT_d = {}
    
    for row in reader:
        key = row[0]
        value = []
        for ranking in row[3:]:
            try:
                value.append(int(ranking))
            except ValueError:
                value.append(ranking)
                
        PT_d[key] = value
        
    return PT_d

