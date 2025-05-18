def AssignCookies(greed,c):
    greed.sort()
    c.sort()
    i = 0
    j = 0
    while i < len(greed) and j < len(c):
        if greed[i] <= c[j]:
                i += 1
        j+=1
    return i
greed = [1,5,3,3,4]
c = [4,2,1,2,1,3]
print(AssignCookies(greed,c))

