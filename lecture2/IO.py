
import sys

class IO:

    def write(self, text):
        print text

    def read(self):
        return sys.stdin.readline().rstrip('\n')