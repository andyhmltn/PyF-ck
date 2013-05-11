PyF*ck
===========================
A Python implementation of the esoteric programming language 'BrainFuck'

Usage
--------	
	from pyfuck import PyFuck

	to_parse = '++++++++++[>++++>++++++++>++++++++++>+++++++++++>++++++++++++<<<<<-]>>.>>>+.<<<----------.<++.>>-.>---.'

	parser = PyFuck(to_parse)
	parser.parse() #=> PyF*ck

Alternate Usage
--------
	import pyfuck
	
	to_parse = '++++++++++[>++++>++++++++>++++++++++>+++++++++++>++++++++++++<<<<<-]>>.>>>+.<<<----------.<++.>>-.>---.'

	pyfuck.parse(to_parse) #=> PyF*ck

Tests
--------

To test, run `test_pyfuck.py`
