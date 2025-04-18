# 2. Write a program to find the sum of elements in a given range [L, R] using a prefix sum array.
def build_prefix_sum(arr):
    prefix= [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

def range_sum(prefix,l,r):
    if l == 0:
        return prefix[r]
    else:
        return prefix[r] - prefix[l-1]
    
#T.C = O(n) , S.C = O(n)
arr = [1,2,3,4,5]
prefix = build_prefix_sum(arr)
l , r = 1, 3
result = range_sum(prefix,l,r)
print(result)