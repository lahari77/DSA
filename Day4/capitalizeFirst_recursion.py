def capitalizeFirst(arr):
    if len(arr) == 0:
        return []
    return [arr[0].capitalize()] + capitalizeFirst(arr[1:])

print(capitalizeFirst(['tom', 'hanks', 'terminal']))

