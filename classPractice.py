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

class StringVarText:
        def __init__(self, array, maxIndex, strings):
            self.list = array
            self.max = maxIndex
            self.strs = strings

        def printString(self, index):
            print(str(self.list[index]) + self.strs[index])

        def setString(self, newString, index):
            self.strs[index] = newString
            return self

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
test = Text(["Hello, user!",
             "This is the 1st line",
             "This is the 2nd line",
             "This is the 3rd line"], 3)

varTest = VarText([" Hello, user!",
                   " This is the 1st line",
                   " This is the 2nd line",
                   " This is the 3rd line"],
                  3,
                  [10, 11, 12, 13])

strTest = StringVarText(["I want to eat a",
                   "I want to eat a",
                   "I want to eat a",
                   "I want to eat a"],
                  3,
                  [" Rutabaga",
                   " Banana",
                   " Carrot",
                   " Pear"])

#****************************************#
#****************************************#
#BEGIN MAIN OUTPUT
#****************************************#
#****************************************#

#Printing initial values of variables
#in all three classes:

print "INITIAL VALUES:"

#Initialize global variable
globalv = 0

#print all data from first class instance
print " "
for i in range(test.max + 1):
        print globalv, test.list[i]
        globalv = globalv + 1

#print all data from second class instance
print " "
for i in range(varTest.max + 1):
        varTest.printString(i)
        globalv = globalv + 1

#print all data from third class instance
print " "
for i in range(strTest.max + 1):
        strTest.printString(i)

print "\nALL VALUES CHANGED:"

#Change globalv to 10
print " "
print "Global counter changed from 0 to 20:"
globalv = 20
                      
#print all data from first class instance
for i in range(test.max + 1):
        print globalv, test.list[i]
        globalv = globalv + 1

print " "
print "Class counter base changed from 10 to 0 with setVal:"
#print all data from second class instance
for i in range(varTest.max + 1):
        varTest.setVal(i, i)
        varTest.printString(i)
        globalv = globalv + 1

print " "
print "Class string variables updated individually with setString method:"
#print all data from third class instance
strTest.setString(" Cat", strTest.max - 3)
strTest.setString(" Dog", strTest.max - 2)
strTest.setString(" Bird", strTest.max - 1)
strTest.setString(" Fish", strTest.max)
for i in range(strTest.max + 1):
        strTest.printString(i)
