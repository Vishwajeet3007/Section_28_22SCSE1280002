from collections import Counter

def max_frequency_element(arr):
    if not arr:
        return None  # Edge case: empty array

    freq = Counter(arr)
    max_elem = max(freq, key=freq.get)
    return max_elem

# Example
arr = [1, 3, 2, 1, 4, 1, 3, 3, 3]
print(max_frequency_element(arr))  # Output: 3
