from array import *
# Creation ( T(n) = O(1))
arr1 = array('i', [1, 2, 3, 4, 5])
print(arr1)
arr2 = array('d', [1.3, 1.5, 1.6])
print(arr2)

# Insertion ( T(n) = O(N))
arr1.insert(6,7)
print(arr1)

arr1 = array('i', [1, 2, 3, 4, 5])
arr1.insert(0,0)
print(arr1)

arr1 = array('i', [1, 2, 3, 4, 5])
arr1.insert(2, 9)
print(arr1)

# Traversing ( T(n) = O(N), S(n) = O(1))
arr1 = array('i', [1, 2, 3, 4, 5])
def traverseArray(array):
    for i in array:
        print(i)
traverseArray(arr1)

# Accessing array element ( T(n) = O(1), S(n) = O(1))
def accessElement(array, index):
    if index >= len(array):
        print("No element present at that index")
    else:
        print(array[index])
accessElement(arr1, 7)
accessElement(arr1, 4)



