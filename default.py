from random import random as rand
from sys import argv

# This regular language is the default
# All it generates is a random number of a's
TERMINAL = ''
NUM_ITERATIONS = 100
ACC_CHANCE = 0.5 #chance that we accept in an accepting state

for i in range(len(argv)):
	arg = argv[i]
	if arg == '-i':
		NUM_ITERATIONS = int(argv[i+1])
	elif arg == '-t':
		TERMINAL = argv[i+1]
	elif arg == '-c':
		ACC_CHANCE = float(argv[i+1])

def reg_lang():
	go = True #loop controller
	state = 0 #our starting state
	output = '' #our output, to be built up

	while go:
		chance = rand()
		if state == 0:
			if rand() <= ACC_CHANCE:
				output += TERMINAL
				go = False
			elif chance >= 0.000:
				output += 'a'
				state = 0
	print(output)

for i in range(NUM_ITERATIONS):
	reg_lang()
