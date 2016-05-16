from random import random as rand
from sys import argv

# This regular language generates strings having an even number of a's and b's

TERMINAL = ''
NUM_ITERATIONS = 100
ACC_CHANCE = 0.5

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
	state = 0
	output = ''

	while go:
		chance = rand()
		if state == 0:
			if rand() <= ACC_CHANCE: #chance that accepting state accepts
				output += TERMINAL
				go = False
			elif chance >= 0.500:
				output += 'a'
				state = 1
			elif chance >= 0.000:
				output += 'b'
				state = 3
		elif state == 1:
			if chance >= 0.500:
				output += 'a'
				state = 0
			elif chance >= 0.000:
				output += 'b'
				state = 2
		elif state == 2:
			if chance >= 0.500:
				output += 'a'
				state = 3
			elif chance >= 0.000:
				output += 'b'
				state = 1
		elif state == 3:
			if chance >= 0.500:
				output += 'a'
				state = 2
			elif chance >= 0.000:
				output += 'b'
				state = 0
	print(output)

for i in range(NUM_ITERATIONS):
	reg_lang()
