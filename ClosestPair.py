import math

def closest_pair_brute_force(points):
    min_dist = float('inf')
    closest_pair = (None, None)

    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = math.hypot(x1 - x2, y1 - y2)  # √((x2-x1)² + (y2-y1)²)
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])

    return min_dist, closest_pair
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
dist, pair = closest_pair_brute_force(points)
print(f"Closest Pair: {pair}, Distance: {dist}")
