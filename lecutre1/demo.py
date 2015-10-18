
__author__ = 'tomasskopal'

import math
import sys

CONST_NAME = "Tomas"

def increment(rawArgs):
    value = int(rawArgs)
    value += 1
    print(value)

def length(rawArgs):
    print("Length of the string: {}".format(len(rawArgs)))

def setPrefix(rawArgs):
    str = "prefix_" + rawArgs
    print("New string: {}".format(str))

def power(rawArgs):
    parsedArgs = rawArgs.split(" ", 1)
    value = math.pow(
        float(parsedArgs[0]),
        float(parsedArgs[1])
    )
    print("Powered value: {}".format(value))

def printMyName():
    print("My name is: {}".format(CONST_NAME))

func_dictionary = {
    "inc": increment,
    "len": length,
    "prefix": setPrefix,
    "power": power,
    "name": printMyName
}

def readStdIn():
    print "Lets Begin. Quit program by typing 'quit'"
    while True:
        userinput = sys.stdin.readline().rstrip('\n')
        if userinput == 'quit':
            break
        else:
            lineArgs = userinput.split(" ", 1)

            if lineArgs[0] not in func_dictionary:
                print "Sorry this function does not exists. Please try again."
                continue

            funct = func_dictionary[lineArgs[0]]
            funct() if len(lineArgs) == 1 else funct(lineArgs[1])

    print "Party ends"

readStdIn()
