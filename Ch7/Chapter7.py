"""
Chapter 1 Solutions 
to Think Python by Robert Downey

Gordon Olwell
November 17, 2017
"""

import math

#7.1
def my_sqrt(a, x):
    while True:
        #print(x)
        y = (x + a/x)/2
        if y == x:
            break
        x = y
    return x

a = my_sqrt(5, 3)

def test_my_sqrt():
    print('{0:1}\t{1:10}\t{2:10}\t{3:10}'.format('a', 
          ' mysqrt', ' math.sqrt', ' diff'))
    #print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
    print("-"*45)
    for i in range(9):
        x = i+1
        n = round(my_sqrt(x, x/2), 10)
        m = round(math.sqrt(i), 10)
        diff = abs(m-n)
        print('{0:1d}\t{1:10f}\t{1:10f}\t{1:10f}'.format(x, n, m, diff))

#test_my_sqrt()

#7.2
def eval_loop():
    x =''
    y = 0
    while True:
        x = input("Provide a number, done to quit: ")
        if x == 'done':
            break
        try: y += eval(x)
        except: 
            print("\nInput not recognized.")
            continue
    print('\nsum = {0}'.format(y))

#eval_loop()
        
