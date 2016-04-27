#!/usr/bin/python
import sys
from math import *


#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    try:
        a=int(float(a))
        b=int(float(b))
        c=int(float(c))
    except ValueError:
        print "One of the inserted values is not a number!"
        exit()
    x1, x2 = find_roots(a, b, c)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):

    mid = b**2 - 4*a*c
    try:
        sqrt_mid = mid**(0.5)
    except ValueError:
        print "The equation has imaginary roots!"
        exit()
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
