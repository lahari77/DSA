# Daily temprature readings
# Day1 - 11,15,10,6
# Day1 - 10,14,11,5
# Day3 - 12,17,12,8
# Day4 - 15,18,4,9

import numpy as np
# Creation
twoDArray = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,4,9]])
print(twoDArray)

# Inserting a column
newcol2Darray = np.insert(twoDArray, 0, [[1,2,3,4]], axis = 1)
print(newcol2Darray)
# Inserting a row
newrow2Darray = np.insert(twoDArray, 0, [[1,2,3,4]], axis = 0)
print(newrow2Darray)
# Inserting a row using append
newrow2Darray1 = np.append(twoDArray, [[1,2,3,4]], axis = 0)
print(newrow2Darray1)

# Accessing
def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect index passed")
    else:
        print(array[rowIndex][colIndex])
accessElement(twoDArray, 2, 3)
accessElement(twoDArray, 3, 1)
accessElement(twoDArray, 2, 10)

# Traversing
def Traverse2Darray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
Traverse2Darray(twoDArray)

# Searching
def search2DArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is at '+str(i)+" "+str(j)
    return 'The element not found'
print(search2DArray(twoDArray, 14))

# Deleting
newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)

