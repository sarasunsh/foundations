# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:00:46 2015

@author: SSunshine
"""
# questions to ask Paul:
#   - I couldn't think of a way to have points in the Test w/o modifying Flashcards. Was I missing something?


from random import shuffle
dash = "-"*30

class Flashcard(object):
     def __init__(self, q, a, p):
        self.question = q
        self.answer = a
        self.points = p
        
     def print_question(self):
        print self.question  

     def print_answer(self):
        print self.answer
        
     def quiz_user(self):
        self.print_question()
        guess = raw_input("Guess: ")
        if guess.lower() == self.answer.lower():
            print "Yup! You got it!"
            print dash
        else:
            print "Nope nope. The correct answer is:", self.answer
            print dash
            
class Test(object):
     def __init__(self, cards):
        self.deck = cards
        self.review = []
        self.correct = 0
        self.total = 0

     def take_test(self):       
         for card in self.deck:
             self.total += card.points
             card.print_question()
             guess = raw_input("Guess: ")
             if guess.lower() == card.answer.lower():
                 self.correct += card.points
             else:
                 self.review.append(card)

     def grade_test(self):
        print "You scored "+str(self.correct)+" points out of a possible "+str(self.total)+"."
        if self.correct < self.total:
            print "You got the following questions incorrect."
            for card in self.review:
                card.print_question()
                card.print_answer()
                print dash
       

easy_cards = [
    Flashcard("What does a cat say?", "meow", 1),
    Flashcard("What is the capital of Vietnam?", "Hanoi", 3),
    Flashcard("What is a Wombat's primary defense?", "rump", 4),
    Flashcard("What is the enemy of laser tag?", "rain", 2),
]

hard_cards = [
    Flashcard("What is a sustained fused action potential called?", "tetanus", 20)]

VALUES = {"What does a cat say?":1, 
"What is the capital of Vietnam?":3, 
"What is a Wombat's primary defense?":4, 
"What is the enemy of laser tag?":2}

first_test = Test(easy_cards)
first_test.take_test()          
#shuffle(cards)       
#for card in cards:
#    card.quiz_user()