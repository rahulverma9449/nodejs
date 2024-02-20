# Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuple are written with round brackets

tuple =  ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple)
print(type(tuple))
# tuple constructor

# index format
print(tuple[-1])
print(tuple[2:5])
print(tuple[:4])
print(tuple[2:])
print(tuple[-2:-1])

# Change Tuple Values
y = ("orange",)
tuple += y
print(tuple)
# y.remove("apple")
# print(tuple)
# Unpacking a Tuple
fruit = ("apple", 'banana', "cherry")
(green, yellow, red) = fruit
print(green)
print(yellow)
print(red)

#########
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(*tropic)
print(red)
mytuple = fruits * 2
print(mytuple)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)





