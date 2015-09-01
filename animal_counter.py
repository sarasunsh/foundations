# -*- coding: utf-8 -*-
"""
Created on Wed May 06 18:57:09 2015

@author: SSunshine
"""

import json
from collections import Counter
 
meow = [
    ['cat', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ['dog', 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    ['rabbit', 11, 21, 31, 41, 51, 61, 71, 81, 91, 11],
    ['mouse', 16, 26, 36, 46, 56, 66, 76, 86, 96, 106],
    ['cat', 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    ['dog', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ['rabbit', 16, 26, 36, 46, 56, 66, 76, 86, 96, 106],
    ['mouse', 11, 21, 31, 41, 51, 61, 71, 81, 91, 11],
]

animal_counter = Counter()
 
for row in meow:
 
    animal_name = row[0]
    animal_counts = row[1:]  # This is a list slice operation, it just cuts out the 0th elemen

    for count in animal_counts:
        animal_counter[animal_name] += count

 
print json.dumps(dict(animal_counter), indent=2)
 
# The output will look like this:
output = {
  "mouse": 1080,
  "dog": 605,
  "rabbit": 1080,
  "cat": 605
}

meow2 = ['cat','cat','cat','cat','cat',
'cat','cat','mouse', 'cat','cat','mouse',
'cat','cat','mouse', 'dog', 'wombat','dog',
'dog','dog', 'mouse', 'rabbit', 'rabbit','rabbit',
'rabbit', 'mouse', 'rabbit','mouse','mouse']

animal_counter2 = Counter()

for thing in meow2:
    animal_counter2[thing] += 1
    
print json.dumps(dict(animal_counter2), indent=2)
