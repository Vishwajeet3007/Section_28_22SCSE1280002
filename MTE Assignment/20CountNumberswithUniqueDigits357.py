def countNumberWithUniqueDigits(n):
    if n == 0:
        return 1
    result = 10
    unique = 9
    available = 9
    for i in range(2,n+1):
        unique *= available
        result += unique
        available -= 1
    return result
n = 3
print(countNumberWithUniqueDigits(n))
n = 2
print(countNumberWithUniqueDigits(n))
n = 1
print(countNumberWithUniqueDigits(n))
