'''
Answers to Chapter
Think Python by Robert Downey
Gordon Olwell
November 9, 2017
'''

#1
4/3*3.14*5**3

#2
(24.95*.6*60)+(3)+(.75*59)

#3
start = 6 + 52 / 60
first_last_mile = 8.15 / 60
middle_mile = 7.12 / 60
total = start + first_last_mile * 3 + middle_mile * 3
print("Time of breakfast is " + str(int(total // 1)) + ":" + 
      str(int((total % 1 * 60)//1)) + ".")
