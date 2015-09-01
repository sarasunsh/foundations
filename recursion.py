# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:26:13 2015

@author: SSunshine
"""

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

def factorial(k):
    if k <= 1:
        return k
    else:
        return k*factorial(k-1)
        
def fib(n):
    if n <= 1:
        return n
    else:
         return fib(n-1) + fib(n-2)
         
#iterative solution to fibonacci, which actually has faster runtime unless you implement a 'memory' (see http://www.python-course.eu/recursive_functions.php)  
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a