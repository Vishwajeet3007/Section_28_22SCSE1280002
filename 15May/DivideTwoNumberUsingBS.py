def divideTwoNumber(dividend,divisor):
    if (dividend or divisor) == 0:
        return
    ans = 0
    left = 0
    right = dividend
    while left <= right:
        mid = (left + right) // 2
        if mid * divisor <= dividend:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
dividend = 10
divisor = 2
print(divideTwoNumber(dividend,divisor))