__author__ = 'tomasskopal'

from functions import increment, length, setPrefix, power, printMyName, printText
import re

class Bot:

    func_dictionary = {
        "inc": increment,
        "len": length,
        "prefix": setPrefix,
        "power": power,
        "name": printMyName,
        "say": printText
    }

    """ constructor """
    def __init__(self, io):
        self.io = io

    def checkRegex(self, text):
        regex = re.compile("\S+")
        for matched in re.findall(regex, text):
            if matched.endswith("--"):
                self.io.decreaseHit(matched[:-2])
            if matched.endswith("++"):
                self.io.increaseHit(matched[:-2])

    def parse(self, userInput):
        lineArgs = userInput.split(" ", 1)

        if lineArgs[0] not in self.func_dictionary:
            self.io.write("Sorry this function does not exists. Please try again.")
            return

        funct = self.func_dictionary[lineArgs[0]]

        if (len(lineArgs) > 1):
            self.checkRegex(lineArgs[1])

        # call function with zero or one argument. It depends on previous parsing. (ternary operator)
        textToPrint = funct() if len(lineArgs) == 1 else funct(lineArgs[1])

        self.io.write(textToPrint)

    def run(self):
        self.io.write("Lets Begin. Quit program by typing 'quit'")
        while True:
            userInput = self.io.read()
            if userInput == 'quit':
                break
            self.parse(userInput)

        print self.io.write("Party ends")

