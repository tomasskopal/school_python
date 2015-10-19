import sys
import re

def run():
	regex = re.compile(sys.argv[1])
	f = open(sys.stdin.readline().rstrip('\n'), 'r')
	for line in f:
        	matched = regex.match(line)
		if(matched):
			print matched.group()
			

run()
