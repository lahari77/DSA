def sumOfDigits(n):
    assert n>=0 and int(n) == n, "N must be a positive integer"
    if n==0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))

print(sumOfDigits(6))
print(sumOfDigits(22))
print(sumOfDigits(134))
print(sumOfDigits(-34))
print(sumOfDigits(2.33))

