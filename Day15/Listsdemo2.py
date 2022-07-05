# Searching element in a list
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# using 'in' operator
if 20 in myList:
    print(myList.index(20))
else:
    print("Element not found")
# using linear search
def searchinList(list, value):
    for i in list:
        if i == value:
            return myList.index(value)
    return 'Element not found'

print(searchinList(myList, 20))
print(searchinList(myList, 100))

# List operations/functions
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(c)
a = [0]
print(a*4)
a = [0, 1]
print(a*4)
a = [0, 1, 2, 3, 4, 5, 6]
print(len(a))
print(max(a))
print(min(a))
print(sum(a)/len(a))

# Test covert below using functions
total = 0
count = 0
while(True):
    inp = input("Enter a value: ")
    if inp == 'done': break
    value = float(inp)
    total += value
    count += 1
    average = total/count
print('Average: ', average)

myList = []
while(True):
    inp = input("Enter a value: ")
    if inp == 'done': break
    myList.append(float(inp))
    average = sum(myList)/len(myList)
print('Average: ', average)

# Lists & Strings
a = 'spam'
b = list(a)
print(b)
a = 'spam spam spam'
b = a.split()
print(b)
a = 'spam*spam*spam'
b = a.split('*')
print(b)
a = '#'.join(b)
print(a)

# Common pitfalls
myList = [3, 1, 2]
myList = myList.sort()
print(myList) # prints None
# 
myList = [3, 1, 2]
myList.append(10)
print(myList)
myList = [3, 1, 2]
myList + [10]
print(myList)
# may mix as
myList = [3, 1, 2]
myList.append([10])
print(myList)
# sort() modify original - no copy maintained
myList = [3, 1, 2]
myList.sort()
print(myList)
# sorted() doesn't modify original - copy maintained
myList = [3, 1, 2]
myList1 = sorted(myList)
print(myList)
print(myList1)

# Arrays vs Lists
#  1. for computations use arrays
import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6])
myList = [1, 2, 3, 4, 5, 6]
print(myArray/2) # [0.5 1.  1.5 2.  2.5 3. ]
# print(myList/2) #error
# list - support diff data, arrray support same data
myArray = np.array([1, 2, 3, 4, 5, 'a'])
myList = [1, 2, 3, 4, 5, 'a']
print(myArray) # ['1' '2' '3' '4' '5' 'a']
print(myList) # [1, 2, 3, 4, 5, 'a']