def permute(arr,l,r):
    #T.C = O(n*n!) S.C=O(n)
    if l == r:
        print(arr)
    else:
        for i in range(l,r+1):
            arr[l] , arr[i] = arr[i] ,arr[l]
            permute(arr,l+1,r)
            arr[l] , arr[i] = arr[i] ,arr[l]
arr = [1,2,3]
permute(arr,0,len(arr)-1)