#!/usr/bin/env python

#########################################
# CLASS PRACTICE
# A script to practice the way python
# classes initialize values
# By Ku3nsting
# March 28, 2017
#########################################

import types

class Text:
    index = None

    def __init__(self, list):
        self.list = list
        
#initialize the class:
test = Text(["Hello, user! This is the 0th line",
                     "This is the 1st line",
                     "This is the 2nd line"])

#change class data member "index" by assignment
Text.index = 2

#print the third item in list
print test.list[Text.index]

#change class data member "index" by assignment
Text.index = 0

#print the 0th item in list
print test.list[Text.index]
