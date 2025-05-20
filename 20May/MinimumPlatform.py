def minimumPlatformNeeded(arr,dep):
    arr.sort()
    dep.sort()
    i = 0
    j = 0
    n = len(arr)
    platform_needed = 0
    max_PlatformNeed = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platform_needed += 1
            max_PlatformNeed = max(max_PlatformNeed,platform_needed)
            i += 1
        else:
            platform_needed -= 1
            j += 1
    return max_PlatformNeed
arr = [900,945,955,1100,1500,1800]
dep = [920,1200,1130,1150,1900,2000]
print(minimumPlatformNeeded(arr,dep))
