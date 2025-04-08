def shipWithinDays(weights,days):
    # Using Brute Force Time Complexity = O(n2) S.C=O(1)
    # def can_ship(capacity):
    #     day = 1
    #     total = 0
    #     for weight in weights:
    #         if total + weight > capacity:
    #             day += 1
    #             total = 0
    #         total += weight
    #     return day <= days

    # min_cap = max(weights)
    # max_cap = sum(weights)

    # for capacity in range(min_cap, max_cap + 1):
    #     if can_ship(capacity):
    #         return capacity

    # # Using Binary Search T.C = O(nlog(n)) S.c= O(1)
    min_cap = max(weights)
    max_cap = sum(weights)
    while min_cap < max_cap:
        mid = min_cap + (max_cap - min_cap) // 2
        day = 1
        summ = 0
        for weight in weights:
            if summ + weight > mid :
                day += 1
                summ = 0
            summ += weight
        if day > days:
            min_cap = mid + 1
        else:
            max_cap = mid
    return min_cap
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights,days))
weights = [3,2,2,4,1,4]
days = 3
print(shipWithinDays(weights,days))
weights = [1,2,3,1,1]
days = 4
print(shipWithinDays(weights,days))