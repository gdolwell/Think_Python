'''
Answers to Cahpter 3
Think Python by Robert Downey
By: Gordon Olwell
Date: November 9, 2017
'''


#3-1
def right_justify(word):
    length = len(word)
    spaces = 70 - length
    print(" "*spaces+word)
    
right_justify("Hello World!")

#3-2
def do_twice(f, value):
    f(value)
    f(value)

def print_spam():
    print('spam')

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)
    
do_twice(print, 'spam')
do_four(print, "Hello World!")

#3.3

def grid_a():
    print("+", "-"*4, "+", "-"*4, "+")

def grid_4a():
    print("+", "-"*4, end=" ")
    print("+", "-"*4, end=" ")
    print("+", "-"*4, end=" ")
    print("+", "-"*4, end=" ")
    print("+")
    
def grid_b():
    print("|", " "*4, "|", " "*4, "|")

def grid_4b():
    print("|", " "*4, "|", " "*4, end=" ")
    print("|", " "*4, "|", " "*4, end=" ")
    print("|")


def grid_box():
    grid_a()
    grid_b()
    grid_b()
    grid_b()
    
def grid_4box():
    grid_4a()
    grid_4b()
    grid_4b()
    grid_4b()

def grid():
    grid_box()
    grid_box()
    grid_a()

grid()

def grid_four():
    grid_4box()
    grid_4box()
    grid_4box()
    grid_4box()
    grid_4a()
    
grid_four()

def add(n1, n2):
    n3 = n1 +n2
    print(n3)
    add(n2, n3)

add(1, 1)
    