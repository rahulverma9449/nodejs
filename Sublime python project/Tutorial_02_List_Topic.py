# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Python Lists
# List items are ordered, changeable, and allow duplicate values.
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist)
mylist.append('apple')
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x)

mylist.extend('apple')
 
print(mylist)
print(len(mylist))
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["juice", "dragan fruit"]
print(thislist)
 
# List Constructor
mylist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))  # Double Round brackets
print(mylist)
# Negative Indexing
print(mylist[-1])
# range o Indexing

print(mylist[2:5])
print(mylist[:4])
print(mylist[2:])
print(mylist[-4:-1])

# While loop
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

# List Comprehension

[print(x) for x in mylist]

newlist = [x for x in mylist if "a" in x]
print(newlist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(4, "watermelon")
print(thislist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]