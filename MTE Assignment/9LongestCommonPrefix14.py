def LongestCommonPrefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    return strs[0]
print(LongestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(LongestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
