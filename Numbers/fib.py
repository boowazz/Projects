#   1 1 2 3 5 8 13 21  <-- here because it's 2am, and I can't brain.

"""Status update: aww shiiet. This doesn't technically solve the problem 
(*sequence* not just Nth element) and more significantly: this runs GOD FUCKING 
SLOW at large values of n. O(2^n) slow. So yeah, that might need fixing."""

def main(n):
    try:
        print fib(int(n))

    
    except ValueError:
        print "uh - that ain't no number, friend. Try again:"
        main(raw_input('Yo, gimme dem digits:'))
        return


def fib(n):
        print n
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        return fib(n-1) + fib(n-2)

main(raw_input("""

Fibonacci
~~~~

Enter a number and have the program generate the Fibonacci sequence to that 
number or to the Nth number.

Yo, gimme dem digits:"""))