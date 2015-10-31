
import sys
import os

class IO:

    def write(self, text):
        print text

    def read(self):
        return sys.stdin.readline().rstrip('\n')

    def decreaseHit(self, person):
        open('hitCounter.txt', 'a').close()  # create file if not exists
        with open('hitCounter.txt', 'r') as input_file, open('temp_counter.txt', 'w+') as output_file:
            founded = False
            for line in input_file:
                splitted = line.split(" ", 1)
                if splitted[0] == person:
                    value = int(splitted[1])
                    value -= 1
                    output_file.write(person + ' ' + str(value) + '\n')
                    founded = True
                else:
                    output_file.write(line)
            if not founded:
                output_file.write(person + ' -1\n')
        os.remove('hitCounter.txt')  # Remove original file
        os.rename('temp_counter.txt', 'hitCounter.txt') #  Move new file


    def increaseHit(self, person):
        open('hitCounter.txt', 'a').close()  # create file if not exists
        with open('hitCounter.txt', 'r') as input_file, open('temp_counter.txt', 'w+') as output_file:
            founded = False
            for line in input_file:
                splitted = line.split(" ", 1)
                if splitted[0] == person:
                    value = int(splitted[1])
                    value += 1
                    output_file.write(person + ' ' + str(value) + '\n')
                    founded = True
                else:
                    output_file.write(line)
            if not founded:
                output_file.write(person + ' 1\n')
        os.remove('hitCounter.txt')  # Remove original file
        os.rename('temp_counter.txt', 'hitCounter.txt') #  Move new file