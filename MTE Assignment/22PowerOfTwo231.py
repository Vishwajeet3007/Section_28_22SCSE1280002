def isPowerOfTwo(n):
    # A power of two is positive and has exactly one bit set 
    # T.C = S.C = O(1)
    # return n > 0 and (n & (n - 1)) == 0

    # T.C  = S.C = O(logn)
    if n <= 0:
        return False
    if n == 1:
        return True
    return (n % 2 == 0 ) and isPowerOfTwo(n//2)


n = 16
print(isPowerOfTwo(n))
n = 20
print(isPowerOfTwo(n))
