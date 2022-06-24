def capitalizeWords(arr):
    if len(arr) == 0:
        return []
    return [arr[0].upper()] + capitalizeWords(arr[1:])

print(capitalizeWords(['hi', 'am', 'learning']))

