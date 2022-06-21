def fibonacci(n):
    assert n>=0 and int(n)==n, "N must be a positive integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))
print(fibonacci(0))
print(fibonacci(-2))
print(fibonacci(2.5))