def findContentChildren(g, s):
    g.sort()  # Sort greed factors
    s.sort()  # Sort cookie sizes
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1  # Child is content
        j += 1  # Move to next cookie
    return i  # Number of content children
g = [1,2,3]
s = [1,1]
print(findContentChildren(g,s))
g = [1,2]
s = [1,2,3]
print(findContentChildren(g,s))