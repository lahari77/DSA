# Integers
integers = [1, 2, 3, 4]
print(integers)
# Strings
stringsList = ['Hi', 'Hii', 'Hiii']
print(stringsList)
# Mixed
mixedList = ['ola', 1.5, 7]
print(mixedList)
# Nested
nestedList = [1, 2, 3, [1.5, 1.6], ['hell']]
print(nestedList)
# Empty
empty = []
print(empty)

# Accessing/Traversing the list
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])
print(shoppingList[1])
print('Milk' in shoppingList)
print('Bread' in shoppingList)
print(shoppingList[-1])
print(shoppingList[-2])
for i in shoppingList:
    print(i)
for i in range(len(shoppingList)):
    shoppingList[i] += '+'
    print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")

# Update/Insert
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)
myList = [1, 2, 3, 4, 5, 6, 7]
myList.insert(0,11)
print(myList)
myList.insert(4, 15)
print(myList)
myList.append(55)
print(myList)
newList = [11, 12, 13, 14]
myList.extend(newList)
print(myList)

# Slicing & Deleting 
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2])
print(myList[:2])
print(myList[1:])
print(myList[:])
myList[0:2] = ['x', 'y']
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(2))
print(myList)
del myList[1]
print(myList)
myList.remove('e')
print(myList)




