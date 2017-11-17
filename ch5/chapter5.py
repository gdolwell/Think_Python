# -*- coding: utf-8 -*-
'''
Chapter 1 Solutions
Think Python by Robert Downey

Gordon Olwell
November 9, 2017
'''

import time
import turtle


#5.1
#convert epoch from seconds to days, hours, minutes and 
seconds = round(time.time() % 60 // 1)
minutes = round(time.time() % (60**2) // 60)
hours = round(time.time() % (60**3) // 60**2)
days = round(time.time() // (24*60*60))

'''print(str(days) + " days " + str(hours) +" hours " + str(seconds)
     + " seconds have past since epoch.")'''


#5.2
'''Fermat's last theorem no n such that a**n +b**n = c**n'''

def check_fermat():
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    n = int(input("N: "))
    while n <= 2 :
        n = int(input("N must be larger than 2. \nN: "))
    if (a**n + b**n == c**n):
        print("\nHoly smokes, Fermat weas wrong!")
    else:
        print("\nNo, that doesn't work.")
        print(str(a**n) + "+" + str(b**n) + "!=" + str(c**n))

#check_fermat()

#5.3
def is_triangle():
    print("This is a program that given three lengths returns if a" +
          " triangle can be formed from those lengths.")
    a = float(input("Length 1: "))
    b = float(input("Length 2: "))
    c = float(input("Length 3: "))
    if ((a+b>=c) & (b+c>=a) & (c+a>=b)):
        print("A triangle can be formed")
    else:
        print("A triangle cannot be formed")

#is_triangle()

#5.5
def koch(t, n):
    """Draws a koch curve with length n."""
    '''input a turtle (t) and length n.'''
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

#bob = turtle.Turtle()
#print(bob)
#koch(bob, 3000)

