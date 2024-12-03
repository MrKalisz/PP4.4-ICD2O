# Lesson plan
  
'''
	Lesson: Lists - indexes, len, combining
	Author: Mr. Kalisz
	Date Created: October 30, 2020
	Date Last Modified: April 8, 2022
'''

#Negative Indexes

#Negative index gives us a value that is at the index specified from the end instead of the beginning

listA = [1, 4, 7, "dog"]

num = listA[-2] #second last index

#Negative values can't be more than the length of the list (also applies to strings)
#Positive Indexes can't be more or equal to the length of the list (Out of bounds)

print(num)

#Combining Lists - combines them side by side using a '+' sign

listB = [3, 4, 5, 6]

listCombined = listA + listB #This will not affect the original two lists, unless you choose to overwrite one of them

#listA = listA + listB - this does overwrite.

print(listCombined)

listCombined = listB + listA

print(listCombined)

#Len - function

#give the length of the list

length = len(listCombined)

print(length)

length = len(listA)

print(length)
