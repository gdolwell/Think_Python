'''
Chapter 11 Solutions 
Think Python by Robert Downey

Gordon Olwell
November 19, 2017
'''

alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j']

my_dict = dict()
for i in range(10):
    my_dict[i] = alphas[i]

#rint(my_dict)

for i in range(12):
    #rint(my_dict.get(i))
    pass


#11.1
fin = open('words.txt')


def words_to_dict(some_fin):
    newdict = dict()
    i = 0
    for line in some_fin:
        newdict[(some_fin.readline().strip())] = i
        i += 1
    return newdict

my_new_dict = words_to_dict(fin)
print(my_new_dict['aah'], my_new_dict['zygote'])

#11.2
