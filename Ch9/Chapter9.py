'''
Chapter 9 Solutions 
Think Python by Robert Downey

Gordon Olwell
November 18, 2017
'''

fin = open('words.txt')



#9.1
def print_word_longer_19(file):
    count = 0
    for word in fin:
        if len(word)>19:
            count += 1
    print('{0} number of words longer than 19.'.format(count))

#print_word_longer_19(fin)

#9.2
fin = open('words.txt')
def contains_no_e(file):
    count1 = 0
    count2 = 0
    for line in file:
        count1 += 1
        word = line.strip()
        if word.find('e') == -1:
            #print(word)
            count2 += 1
    print(count2, count1, count2/count1)
    
#contains_no_e(fin)

#9.3
def avoids(word, letters):
    result = True
    for letter in letters:
        if word.find(letter) == -1:
            continue
        else:
            result = False
    return result

#print(avoids('banana', 'cde'))


#9.5
def uses_all(word, letters):
    result = True
    for letter in letters:
        if word.find(letter) != -1:
            continue
        else:
            result = False
    return result

#print(uses_all('banana', 'ban'))

#9.6
def is_abc(word):
    result = True
    for i in range(len(word)):
        if i < len(word)-1:
            if ord(word[i])<=ord(word[i+1]):
                continue
            else:
                result = False
    return result


#print(is_abc('banana'))
#print(is_abc('abcdnop'))

 #9.7
       

