#tupple: NOT MUTABLE import sys
# write,
# print 3rd element,
# print all elements [dont use name of tuple :P],
# check if there is elements in tuple, check the length, count elements,
# how many 0 is included in tuple,
# find index od -3 element (by its value)
# covert to list, print both type,
# slicing, step 3, * reverse
# pack and unpack
# time of process 1.000.000 times, and bits. sys.getsizeof(type_name) "bytes") timeit.timeit(stmt+"[tuple], number = 10000000]
# - > solve numeric /string variables - how to add item to th

import sys
import timeit
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))


ideal_girl = ("Puyin", 1830, 'Thai', "aahan_phed")

item = ideal_girl[-2]
print("item index -2 is:" + item)
print(ideal_girl[2])

for i in ideal_girl:
    print(i)

is_in_tuple = input("Check if element belong to tuple: ")
if is_in_tuple in ideal_girl:
    print("It is!")
else:
    print("sorry")

#length of tuple (number of elements
print(len(ideal_girl))

#count of object '1830' in tuple
print(ideal_girl.count(1830))

#index of element 1830 in tuple
print(ideal_girl.index(1830))

# check type of
print(type(ideal_girl))

# convert tuple into list
ideal_girl_list = list(ideal_girl)
tuple2 = tuple(ideal_girl_list)

print(ideal_girl)
print(sys.getsizeof(ideal_girl), 'bytes')
print(ideal_girl_list)
print(sys.getsizeof(ideal_girl_list), bytes)
print(tuple2)
print(sys.getsizeof(tuple2), bytes)


# compress uncompress zip/unzip tuple with demonstrate *
tuple3 = ("Jetty", "Bangkok", 28, 1991, 69)
name, city, *position = tuple3

print(name)
#print(age)
print(city)
print(position)
#print(year)

