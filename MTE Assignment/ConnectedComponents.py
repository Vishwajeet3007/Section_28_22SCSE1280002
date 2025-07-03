from collections import defaultdict
def count_components(n, edges):
    # Step 1: Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    count = 0
    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(i)
            count += 1

    return count
n = 5
edges = [[0, 1], [1, 2], [3, 4]]

# Graph:
# 0 - 1 - 2    3 - 4
# => Two components

print(count_components(n, edges))  # Output: 2
