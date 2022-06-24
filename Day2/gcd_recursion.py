def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers should be integers."
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(48, 12))
print(gcd(-8, 12))
print(gcd(12.2, 4))
