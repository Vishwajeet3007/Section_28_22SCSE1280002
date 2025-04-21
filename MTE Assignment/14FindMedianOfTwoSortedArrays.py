# USing Binary Search
def findMedianOfTwoSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # Handle edges
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        # Found correct partition
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:
                return float(max(maxLeftX, maxLeftY))
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1

# Using Brute Force

# def findMedianOfTwoSortedArrays(nums1,nums2):
#     merged_list = nums1 + nums2
#     merged_list.sort()
#     length_of_merged_list = len(merged_list)
#     if length_of_merged_list % 2 == 1:
#         return float(merged_list[length_of_merged_list//2])
#     else:
#         mid1 = merged_list[length_of_merged_list//2 - 1]
#         mid2 = merged_list[length_of_merged_list // 2]
#         return (float(mid1) + float(mid2)) / 2.0
nums1 = [1,2]
nums2 = [3]
print(findMedianOfTwoSortedArrays(nums1,nums2))
nums1 = [1,2]
nums2 = [3,4]
print(findMedianOfTwoSortedArrays(nums1,nums2))
