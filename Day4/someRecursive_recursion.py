def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not cb(arr[0]):
        return someRecursive(arr[1:], cb)
    return True

print(someRecursive([1, 2, 3, 4], isOdd)) # True
print(someRecursive([4, 6, 8, 9], isOdd)) # True
print(someRecursive([4, 6, 8], isOdd)) #False

