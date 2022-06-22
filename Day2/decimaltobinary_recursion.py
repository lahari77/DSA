def decimalToBinary(n):
    assert int(n) == n, "Number should be an integer"
    if n == 0:
        return 0
    return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(10))
print(decimalToBinary(3))
print(decimalToBinary(-5))
print(decimalToBinary(22.4))

