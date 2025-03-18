def rangeSumquries(arr,queries):
    
    # summ = []
    # for i in range(len(queries)):   
    #     start,end = queries[i]
    #     summ.append(sum(arr[start:end + 1]))
    # return summ                              # T.C. = O(Q*N) and S.C.= O(q)

    prefix_sum = [0] * (len(arr)+1)
    for i in range(len(arr)):
        prefix_sum[i+1] += prefix_sum[i] + arr[i]
    result = []
    for start,end in queries:
        result.append(str(prefix_sum[end + 1]-prefix_sum[start]))
    return " ".join(result)                  # T.C and S.C. = O(Q+N)

arr = [3,1,4,1,5,9]
queries = [(1,3),(0,2),(2,5)]
print(rangeSumquries(arr,queries))
