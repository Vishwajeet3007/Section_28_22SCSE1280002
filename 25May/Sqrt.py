def sqrt(n,low ,high):
    if n == 0 or  n== 1:
        return n
    if low > high:
        return high
    mid = (low + high) // 2
    if mid * mid == n:
        return mid
    if mid * mid < n:
        return sqrt(n,mid + 1 ,high)
    else:
        return sqrt(n,low ,mid - 1)
n = 25
print(sqrt(n,0,25))    
n = 49
print(sqrt(n,0,49))