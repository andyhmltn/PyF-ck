PyF*ck
===========================
A Python implementation of the esoteric programming language 'BrainFuck'

Usage
--------	
	from pyfuck import PyFuck

	to_parse = '++++++++++[>++++>++++++++>++++++++++>+++++++++++>++++++++++++<<<<<-]>>.>>>+.<<<----------.<++.>>-.>---.'

	parser = PyFuck(to_parse)
	parser.parse() #=> PyF*ck
