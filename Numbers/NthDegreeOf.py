from mpmath import *

def main(sigfig):
	try:	
		if int(sigfig) > 10000:
			print 'uh, too big dude/dudette.'
			return
		else:
			mp.dps = sigfig #specifying the precision
			print +pi
			return
	
	except ValueError:
		print "uh - that ain't no number, friend. Try again:"
		main(raw_input('Yo, gimme dem digits:'))
		return

main(raw_input("""
Nth Degree of Pi
~~~~
Enter a number and have the program generate PI up to that many 
decimal places. Keep a limit to how far the program will go.

Hokay, scho, gimme dem digits:"""))

