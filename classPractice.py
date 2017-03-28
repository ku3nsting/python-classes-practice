#!/usr/bin/env python

##########################################
# CLASS PRACTICE                         #
# A script to practice the way python    #
# classes initialize values              #                         
# March 28, 2017                         #
##########################################

import types

#****************************************#
#INITIALIZE CLASS (to hold text component)
#****************************************#

class VarText:
        def __init__(self, array, maxIndex, values):
            self.list = array
            self.max = maxIndex
            self.vals = values

        def printString(self, index):
            print(str(self.vals[index]) + self.list[index])

        def setVal(self, newVal, index):
            self.vals[index] = newVal
            return self

        def updateObject(self, newString, newValue):
            self.list.append(newString)
            self.vals.append(newValue)
            self.max = len(self.vals)-1

class Text:
        def __init__(self, array, maxIndex):
            self.list = array
            self.max = maxIndex

#****************************************#
#TEST function to print variable both
#directly and from the class data
#****************************************#
def printTest(v, i):
        #call print function on globalv directly:
        print "Directly accessing globalv", v

        #print it from the class:
        print "Printing from class:"
        print i
        
#****************************************#
#INITIALIZE TEXT COMPONENTS
#initialize all non-variable lines:
#****************************************#
test = Text([" Hello, user!",
             "This is the 1st line",
             "This is the 2nd line",
             "This is the 3rd line"], 3)

varTest = VarText([" Hello, user!",
                   " This is the 1st line",
                   " This is the 2nd line",
                   " This is the 3rd line"],
                  3,
                  [10, 11, 12, 13])

#****************************************#
#****************************************#
#BEGIN MAIN OUTPUT
#****************************************#
#****************************************#

#Initialize global variable
globalv = 0

#print all data from first class instance
print "\n"
for i in range(test.max + 1):
        print globalv, test.list[i]
        globalv = globalv + 1

#print all data from second class instance
print "\n"
for i in range(varTest.max + 1):
        varTest.printString(i)
        globalv = globalv + 1

#Change globalv to 10
globalv = 20
                      
#print all data from first class instance
print "\n"
for i in range(test.max + 1):
        print globalv, test.list[i]
        globalv = globalv + 1

#print all data from second class instance
print "\n"
for i in range(varTest.max + 1):
        varTest.setVal(i, i)
        varTest.printString(i)
        globalv = globalv + 1
