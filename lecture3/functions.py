__author__ = 'tomasskopal'

import math

CONST_NAME = "Tomas"

def increment(rawArgs):
    value = int(rawArgs)
    value += 1
    return value

def length(rawArgs):
    return "Length of the string: {}".format(len(rawArgs))

def setPrefix(rawArgs):
    str = "prefix_" + rawArgs
    return "New string: {}".format(str)

def power(rawArgs):
    parsedArgs = rawArgs.split(" ", 1)
    value = math.pow(
        float(parsedArgs[0]),
        float(parsedArgs[1])
    )
    return "Powered value: {}".format(value)

def printMyName():
    return "My name is: {}".format(CONST_NAME)

def printText(text):
    return text