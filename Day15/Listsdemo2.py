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