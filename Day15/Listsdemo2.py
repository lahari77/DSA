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

