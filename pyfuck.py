## Import System for writing to STDOUT ##
import sys

class PyFuck:
	def __init__(self, string, log = False):
		## This is the string (IE: BrainFuck Code) that the class will parse
		self.string  = string
		## The current position of the counter
		self.counter = 0
		## The complete memory set (Limited from 30,000 to 300)
		self.memory  = [0] * 300
		## This is used when a loop is declared as the start of said loop
		self.loop    = 0
		## This is for debug purposes
		self.log     = log

	## Declare the Parser
	def parse(self):
		## Correspond the characters to their appropriate functions
		options = {
			'+':self.plus,
			'-':self.minus,
			'>':self.forward,
			'<':self.backward,
			'[':self.begin_loop,
			']':self.end_loop,
			'.':self.output
		}

		## Using a while loop instead of a for loop so we can manipulate 'i'
		i = 0
		while i < len(self.string):
			## Current character being parsed
			current_char = self.string[i]

			## Each function should return a manipulation (or an indentical version) of i
			i = options[current_char](i)
			
			## Log each transaction
			if self.log: print "Transaction: (counter:"+str(self.counter)+") " + str(current_char) + " Result: " + str(self.memory[self.counter]) + " (i: "+str(i)+")"

		## Write a newline at the end
		sys.stdout.write('\n')

	## Add 1 to the current cell
	def plus(self, i):
		self.memory[self.counter] += 1
		return i + 1

	## Minus 1 from the current cell
	def minus(self, i):
		self.memory[self.counter] -= 1
		return i + 1

	## Move the counter forward
	def forward(self, i):
		self.counter += 1
		return i + 1

	## Move the counter backward
	def backward(self, i):
		self.counter -= 1
		return i + 1

	## Begin the loop
	def begin_loop(self, i):
		## Mark where the loop started
		self.loop = i
		return i + 1

	## End the loop
	def end_loop(self, i):
		## If the current cell isn't 0, then return to where the loop started
		if(self.memory[self.counter] != 0):
			return self.loop
		else:
			return i + 1

	## Outputs the current cell
	def output(self, i):
		sys.stdout.write(chr(self.memory[self.counter]))
		return i + 1

	## Dump the entire memory set. Useful for debugging
	def dump(self):
		for i in self.memory:
			print i
