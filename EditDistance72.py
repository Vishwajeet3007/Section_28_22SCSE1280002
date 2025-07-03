def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # insert all characters

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation needed
            else:
                insert_op = dp[i][j - 1] + 1
                delete_op = dp[i - 1][j] + 1
                replace_op = dp[i - 1][j - 1] + 1
                dp[i][j] = min(insert_op, delete_op, replace_op)

    return dp[m][n]
print(minDistance("horse", "ros"))
# Output: 3
# Explanation: horse -> rorse (replace 'h' with 'r')
#              rorse -> rose (remove 'r')
#              rose -> ros (remove 'e')
