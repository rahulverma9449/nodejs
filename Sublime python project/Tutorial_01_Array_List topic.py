
# Online Python - IDE, Editor, Compiler, Interpreter
#Array are used to store multiple values in one single variable.
cars = ["Ford", "volvo", "BMW"]
cars[0] = "Toyota"

cars.count()
print(cars)
#loop
for x in cars:
    print(x)
print(cars)
print(len(cars))

# Adding Array Elements
cars.append("Hondo City")
print(cars)

# Removing Array Elements
# used pop() Method/Function

# cars.pop(2)
cars.remove('volvo')
print(cars)

# python has a set of built in method that you can use on lists/arrays
# cars.clear() # clear method
# print(cars)

fruit = ['apple', 'banana', 'apple', 'cherry', 'orange']
# x = fruit.count('apple')
fruit.extend(cars)
print(fruit)
# index() method

x = fruit.index('cherry')
print(x)

# List Insert() method
fruit.insert(1, "pineapple")
print(fruit)

# List pop() method

fruit.pop(1)
print(fruit)

# List Reverse() method

fruit.reverse()
print(fruit)

# List Sort() method
# The sort() method sorts the list ascending by default
cars.sort()
fruit.sort()
print(cars)
print(fruit)

def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
from array import *

array1 = array('i', [10,20,30,40,50])

# print(array1[0])
# print(array1[2])

### Inserting Operation

# array1.insert(1, 35)

# for x in array1:
# 	print(x)

### Deletion Operation

# array1.remove(40)
# for x in array1:
# 	print(x)

### Search Operation

print(array1.index(50))

### Update Operation

array1[2] = 100

for x in array1:
	print(x)


# Reverse an Array

arr=[5,7,4,2,3,8,11,6]
arr.append(9)
key = 8
arr.remove(key)
print(arr)
arr = sorted(arr, reverse=True)
print(arr)
def reverse(arr):
    low = 0
    high = len(arr)-1
    while low<high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

print("orignal array is: ", arr)
reverse(arr)
print("New array reverse is : ", arr)



