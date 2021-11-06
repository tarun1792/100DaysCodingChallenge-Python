from sys import maxint
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = -maxint - 1
        minEndingHere = 0
        size = len(nums)
        
        for i in range(0,size):
            
            minEndingHere = minEndingHere + nums[i]
            
            if maxSoFar < minEndingHere:
                maxSoFar = minEndingHere
                
            if minEndingHere < 0:
                minEndingHere = 0
                
        return maxSoFar
