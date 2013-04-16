PyF*ck
===========================
A Python implementation of the esoteric programming language 'BrainFuck'

Usage
--------	
	from pyfuck import BrainFuck

	to_parse = '++++++++++[>++++>++++++++>++++++++++>+++++++++++>++++++++++++<<<<<-]>>.>>>+.<<<----------.<++.>>-.>---.'

	parser = BrainFuck(to_parse)
	parser.parse() #=> PyF*ck
