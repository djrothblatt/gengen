#Regular Language Generator
from sys import argv 

OUT_FILE = "default.py"
states = {}
start = None
accs  = []

#############################################################
#							    #
# 		GETTING THE ARGUMENTS			    #
#							    #
#############################################################

def get_trans(args, i):
	dests = [] #a destination is a pair (label, emission), where label is a natural, emission is a character
	state = int(args[i]) #grab the state
	i += 1 
	while i < len(args) and args[i][0] != '-': #while not looking at a flag
		dests.append((args[i], args[i+1])) #add (label, emission) to list of destinations
		i += 2 #then look at the next label/emission pair
	return state, dests

#gets the position of the next argument
def get_next(args, i):
	while i < len(args) and args[i][0] != "-":
		i += 1
	return i

i = 1
FLAGS = ["-n", "-s", "-a", "-sa", "-o", "-h"]
STATE_FLAGS = ["-n", "-s", "-a", "-sa"]
STARTERS = ["-s", "-sa"]
ACCEPTORS = ["-a", "-sa"]
while i < len(argv):
	arg = argv[i]
	if arg in STATE_FLAGS:
		state, dests = get_trans(argv, i+1) #no matter what kind of state, we need to get the transitions...
		states[state] = dests #and record them in our dictionary of states
		if arg in STARTERS:
			start = state 
		if arg in ACCEPTORS:
			accs.append(state)
	elif arg == "-o":
		OUT_FILE = argv[i+1]
	elif arg == "-h":
		print("Sorry, the help text has not been written yet.")
		print("Please consult the comments at the head of this program for instructions")
		exit(0)
	else:
		print("Please feed in valid arguments as specified in the help text")
		exit(1)
	i = get_next(argv, i+1)


#############################################################
#	    						    #
#        	PRINTING TO DESIGNATED OUT_FILE             #
#							    #
#############################################################

#PROGRAMMER'S COMMENTS:
#This code looks kinda weird, but it's code that creates code, so maybe that makes sense
#Still, it could probably use some cleaning up...

f = open(OUT_FILE, "w")
def p(message): #unexpectedly robust; format codes welcome!
    print(message, file = f)

def create_state(transitions, acc = False):
	started = False
        length = len(transitions)
        step = 1.0 / length #spreads transitions out evenly
	threshold = 1.0
	if acc:
		p("\t\t\tif rand() <= ACC_CHANCE:")
		p("\t\t\t\toutput += TERMINAL")
		p("\t\t\t\tgo = False")
		started = True
	i = 0
	while threshold >= 0 and i < length:
		whether = "if" if not started else "elif"
		p("\t\t\t%s chance >= %.3f:" %(whether, threshold - step))
		p("\t\t\t\toutput += '%s'" %(transitions[i][1]))
		p("\t\t\t\tstate = %s" %(transitions[i][0]))
		threshold -= step
		i += 1
		started = True
#header
p("from random import random as rand\nfrom sys import argv\n")
p("TERMINAL = ''\nNUM_ITERATIONS = 100\nACC_CHANCE = 0.5 #chance that we accept in an accepting state\n")

#get arguments
p("for i in range(len(argv)):")
p("\targ = argv[i]")
p("\tif arg == '-i':")
p("\t\tNUM_ITERATIONS = int(argv[i+1])")
p("\telif arg == '-t':")		
p("\t\tTERMINAL = argv[i+1]")	
p("\telif arg == '-c':")
p("\t\tACC_CHANCE = float(argv[i+1])\n")

#main definition
p("def reg_lang():")
p("\tgo = True #loop controller")
p("\tstate = %d #our starting state" %(start))
p("\toutput = '' #our output, to be built up\n")

p("\twhile go:")
p("\t\tchance = rand()")
started = False
for state, transitions in states.items():
	whether = "if" if not started else "elif"
	p("\t\t%s state == %d:" %(whether, state))
	create_state(transitions, state in accs)
	started = True
p("\tprint(output)\n")

#control
p("for i in range(NUM_ITERATIONS):")
p("\treg_lang()")
f.close()
print("%s is created! Whyncha give a look?" %(OUT_FILE))
