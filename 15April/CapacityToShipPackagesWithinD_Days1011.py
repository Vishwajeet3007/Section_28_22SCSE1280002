def maxCapacity(weights,days):
    min_cap = max(weights)
    max_cap = sum(weights)
    while min_cap < max_cap:
        mid = min_cap + (max_cap - min_cap) // 2
        day = 1
        summ = 0
        for weight in weights:
            if summ + weight > mid:
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
print(maxCapacity(weights,days))
weights = [3,2,2,4,1,4]
days = 3
print(maxCapacity(weights,days))