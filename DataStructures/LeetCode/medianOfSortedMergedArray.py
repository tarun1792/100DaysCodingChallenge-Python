# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        mergedArray = []
        i = 0
        j = 0
        
        while (i < len(nums1)) and (j < len(nums2)):
             
            if nums1[i] <= nums2[j]:
                mergedArray.append(nums1[i])
                i += 1
            else: 
                mergedArray.append(nums2[j])
                j += 1
                
            
        while i < len(nums1):
            mergedArray.append(nums1[i])
            i += 1
            
        while j < len(nums2):
            mergedArray.append(nums2[j])
            j += 1
            
        mergedArrayLength = len(mergedArray)
        mid = int(mergedArrayLength / 2)
        
        if mergedArrayLength % 2 == 0:
            mid1 = mergedArray[mid - 1]
            mid2 = mergedArray[mid]
            median = (mid1 + mid2)/2
        else:
            median = mergedArray[mid]
            
        return median