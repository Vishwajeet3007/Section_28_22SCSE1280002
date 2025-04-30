def is_palindrome(x):
    # if x < 0:
    #     return False
    # original = x
    # reversed_num = 0
    # while x > 0:
    #     digit = x % 10
    #     reversed_num = reversed_num * 10 + digit
    #     x = x // 10
    # return original == reversed_num

# Using Two Pointers
    x = str(x)
    n = len(x)
    left = 0
    right = n  - 1
    while left <= right:
        if x[left] == x[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(is_palindrome(121))
print(is_palindrome(123))