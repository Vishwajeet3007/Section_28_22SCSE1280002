import math
def minEatingSpeed(piles, h):
        left = 1
        right = max(piles)
        def canFinish(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))