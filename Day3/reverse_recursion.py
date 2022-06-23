def reverse(strng):
    if len(strng) in [0,1]:
        return strng
    return strng[-1] + reverse(strng[:-1])

print(reverse('python'))
print(reverse('structures'))

