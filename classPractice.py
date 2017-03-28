#!/usr/bin/env python

##########################################
# CLASS PRACTICE                         #
# A script to practice the way python    #
# classes initialize values              #
# By Ku3nsting                           #
# March 28, 2017                         #
##########################################

import types

#****************************************#
#INITIALIZE CLASS (to hold text component)
#****************************************#
class Text:
        index = 0
        def __init__(self, array, maxIndex):
            self.list = array
            self.max = maxIndex

#****************************************#
#TEST function to print variable both
#directly and from the class data
#****************************************#
def printTest(v, i):
        #call print function on globalv directly:
        print "Directly accessing globalv: {}".format(v)

        #print it from the class:
        print "Printing from class:"
        print i
        
#****************************************#
#INITIALIZE TEXT COMPONENTS
#initialize all non-variable lines:
#****************************************#
test = Text(["Hello, user!",
             "This is the 1st line",
             "This is the 2nd line",
             "This is the 3rd line"], 3)


#****************************************#
#****************************************#
#BEGIN MAIN OUTPUT
#****************************************#
#****************************************#

#Initialize global variable
globalv = 0

#change class data member "index" by assignment
Text.index = 2

#print all data from first class instance
for i in range(test.max + 1):
        print globalv, test.list[i]
        globalv = globalv + 1

#Change global variable to 7
globalv = 7

#****************************************#
#INITIALIZE VARIABLE-ENHANCED TEXT
#initialize variable lines as needed:
#necessary because variables inside class
#data member arrays seem to have a local
#scope, and can't be changed after they
#are initialized
#****************************************#
varLine = Text(["This line contains globalv, which holds: {}".format(globalv)], 0)

print varLine.list[varLine.max]

#change value of globalv
print "Directly accessing globalv: {}".format(globalv)
print "\nUpdate value of globalv to 9"
globalv = 9
print "Directly accessing globalv: {}".format(globalv)

#Try to change and re-print variable
#doesn't work, despite the fact that "global" has changed outside of the class
print "\nfirst try:"

printTest(globalv, varLine.list[varLine.max])

#Change variable by re-initializing class
print "\nsecond try:"
varLine = Text(["This line contains globalv, which holds: {}".format(globalv)], 0)

printTest(globalv, varLine.list[varLine.max])









