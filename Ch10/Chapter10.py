'''
Chapter 10 Solutions 
Think Python by Robert Downey

Gordon Olwell
November 18, 2017
'''



#10.1
def nested_sum(nested):
    total = 0
    for x in nested: 
        for i in x:
            total += i
    return total
    
x = [[1, 2, 3], [4, 5, 6]]
#print(nested_sum(x))


#10.2
def cum_sum(some_list):
    z = []
    for i in range(len(some_list)):
        if i == 0:
            z.append(some_list[i])
        else:
            z.append(some_list[i] + z[i - 1])
    return z
     
y = [1, 2, 3]
#print(cum_sum(y))

#10.3
def middle(some_list):
    new_list = []
    for i in range(len(some_list)):
        if i == 0:
            continue
        elif i == len(some_list) - 1:
            #print(i)
            continue
        else:
            new_list.append(some_list[i])
    return new_list

a = [1, 2, 3, 4, 5]
#print(middle(a))

#10.4
def chop(some_list):
    for i in range(len(some_list)):
        if i == 0 or i == len(some_list) - 1:
            some_list.pop(i)
    return None

b = [1, 2, 3, 4]
chop(b)
#print(b)

#10.5
def is_sorted(some_list):
    new_list = []
    for i in some_list:
        new_list.append(i)
    new_list.sort()
    #print(some_list, new_list)
    #print(new_list == some_list)

is_sorted([1, 2, 3, 4, 5])
is_sorted([5, 4, 3, 2, 1])

#10.6
def is_anagram(word1, word2):
    new1 = list(word1)
    new2 = list(word2)
    new1.sort()
    new2.sort()
    if new1 == new2:
        return True
    else:
        return False

#print(is_anagram('west', 'stew'))
#print(is_anagram('wests', 'stew'))

#10.7
def has_duplicates(some_list):
    new_list = []
    result = False
    for i in some_list:
        new_list.append(i)
    new_list.sort()
    for i in range(len(new_list) - 1):
        if new_list[i] == new_list[i+1]:
            result = True
    return result

#print(has_duplicates(list('jumpshot')), has_duplicates('sass'))
