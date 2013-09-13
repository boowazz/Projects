#   1 1 2 3 5 8 13 21  <-- here because it's 2am, and I can't brain.

from math import *


def main(n):
    try:
        for i in range(0,int(n)):
            print fib(int(i)), #comma on the end to add space.

    
    except ValueError:
        print "uh - that ain't no number, friend. Try again:"
        main(raw_input('Yo, gimme dem digits:'))
        return


def fib(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
    #formula for calculating nth fibonacci number - source:
    # wolfram alpha

'''
Recursive attempt, but damn slow. O(2^n) slow.

def fib(n):
        print n
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        return fib(n-1) + fib(n-2)
'''


main(raw_input("""

Fibonacci
~~~~

Enter a number and have the program generate the Fibonacci sequence to that 
number or to the Nth number.

Yo, gimme dem digits:"""))