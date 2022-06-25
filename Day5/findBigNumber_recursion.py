from gettext import find


arr= [10, 2, 3, 4, 5]
def findBigNumber(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n-1], findBigNumber(arr, n-1))

print(findBigNumber(arr, len(arr)))

