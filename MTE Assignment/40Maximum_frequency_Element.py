from collections import Counter
def max_frequency_element(nums):
    freq = Counter(nums)
    max_element = max(freq,key=freq.get)
    max_freq = freq[max_element]
    #max_elem, max_freq = Counter(arr).most_common(1)[0]
    return max_freq
arr = [1, 3, 2, 1, 4, 1, 3, 3, 3]
print(max_frequency_element(arr))
