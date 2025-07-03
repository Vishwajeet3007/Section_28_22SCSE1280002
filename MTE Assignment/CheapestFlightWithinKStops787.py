import heapq
from collections import defaultdict

def find_cheapest_price(n, flights, src, dst, k):
    # Build graph: adjacency list {from: [(to, price), ...]}
    graph = defaultdict(list)
    for u, v, cost in flights:
        graph[u].append((v, cost))
    
    # Priority queue: (cost so far, current node, stops made)
    heap = [(0, src, 0)]

    # (node, stops) → minimum cost seen so far
    visited = {}

    while heap:
        cost, node, stops = heapq.heappop(heap)

        # If destination is reached within k+1 flights (k stops means k+1 flights)
        if node == dst:
            return cost

        # If we can still take more flights
        if stops <= k:
            for nei, price in graph[node]:
                next_cost = cost + price

                # Only consider this path if it's cheaper or we haven't visited this stop count before
                if (nei, stops) not in visited or visited[(nei, stops)] > next_cost:
                    visited[(nei, stops)] = next_cost
                    heapq.heappush(heap, (next_cost, nei, stops + 1))
    
    return -1  # No route within k stops

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

print(find_cheapest_price(n, flights, src, dst, k))  # Output: 700
