def countBits(n):

    #return [bin(i).count('1') for i in range(n + 1)] # T.C = O(nlogn) S.C = O(logn)

    # T.C =  S.C = O(n)  
    result = [0] * (n+1)
    for i in range(1,n+1):
        if i % 2 != 0:
            result[i] = result[i//2] + 1
        else:
            result[i] = result[i//2]

    return result 