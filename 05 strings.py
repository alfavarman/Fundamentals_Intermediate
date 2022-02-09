# Strings: ordered, immutable, text represenation
# with "" or '' - useful if you want include "I'm" otherwise /
# """ all writen in this field will look like its typed / ->will prevent to move to next line """
# print string - long sentence
# Slicing substring  from 2 lettet to 12, # from 10 till end # every 3rd letter
# Remove white space from "             Charles is the best Khru            "
# convert to upper case
# check if starts with False
# check with ends with Khru
# check index of b
# count how many e is in
# replace charles with your name
# split this sentence to the list
# make new string with comas in stead of  space from list
# Compare 2 methods of converting list to string and prove one is better 1:17:22 write new
# %, .format(), f-string


# CONVERTING LIST TO STRING
import sys
from timeit import default_timer as time
list = ['abc'] * 100000
list2 = list.copy()

# Method For loop
start = time()
string1 = ''
for x in list:
    string1 += x
stop = time()
#print(string1)
print('time: ',start-stop)
print(sys.getsizeof(string1), bytes)


# Method .join
start = time()
string2 = ''.join(list2)
stop = time()
#print(string2)
print('time: ', start-stop)
print(sys.getsizeof(string2), bytes)
