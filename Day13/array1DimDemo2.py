from array import *
arr1 = array('i', [1,2,3,4,5,6])
def searchElement(array, value):
    for i in array:
        if i == value:
            return array.index(i)
    return "The element not found in array"


print(searchElement(arr1, 3))
print(searchElement(arr1, 6))
print(searchElement(arr1, 7))

# Deleting elements
arr2 = [1,2,3,4,5,6]
arr2.remove(1)
print(arr2)
arr2.remove(6)
print(arr2)
arr2.remove(4)
print(arr2)