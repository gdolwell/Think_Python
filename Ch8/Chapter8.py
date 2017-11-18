"""
Chapter 8 Solutions 
Think Python by Robert Downey

Gordon Olwell
November 18, 2017
"""

#8.1
words = '     Hello python world!      '
print(words.strip())
print(words.find('o'))

#8.2
print('banana'.count('a'))

#8.3
def is_palindrome(word):
    if word[::] == word[::-1]:
        return True
    else:
        return False

print(is_palindrome('able was I ere I saw elba'))

#8.4
def rotate_word(word, x):
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    for letter in word:
        letter =  (alphas[(ord(letter)-97+x)%26])
        print(letter)
        
    return word
        
print(rotate_word('cheer', 7))

