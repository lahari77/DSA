def flatten(arr):
    resultArr = []
    for element in arr:
        if type(element) == list:
            resultArr.extend(flatten(element))
        else:
            resultArr.extend([element])
    return resultArr

print(flatten([1, 2, 3, [4, 5]]))
print(flatten([1, [2, [3, 4], [[5]]]]))
print(flatten([[1], [2], [3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))

