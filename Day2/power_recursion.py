def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "Exponent should be a positive integer"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp-1)

print(power(3,6))
print(power(-2, 4))
print(power(2.5, 2))
print(power(3, -1))
print(power(2.5, 1.2))



