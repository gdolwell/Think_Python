"""
Chapter 1 Solutions 
to Think Python by Robert Downey

Gordon Olwell
November 17, 2017
"""

#6.2
def ack(x, y):
    if (x == 0):
        y = y+1
        return y
    elif (y ==0):
        return ack(x-1, 1)
    else:
        return ack(x-1, ack(x, y-1))


#print (ack(3, 4))

#6.3
def is_palindrome(word):
    for i in range(len(word)//2):
        #print(word[i], word[-(i+1)])
        
        if(word[i] == word[-(i+1)]):
            #print(i, word[i])
            continue
        else:
            return False
    return True

#a = is_palindrome("momom")
#print(a)

#6.4    
def is_power(a, b):
    if (a%b == 0):
        if((a/b)%b==0):
            print("True")
        else:
            print("False")
    else:
        print("False")

#is_power(125, 5)
#is_power(24, 3)
#is_power(4, 2)

#6.5
def gcd(a, b):
    pass