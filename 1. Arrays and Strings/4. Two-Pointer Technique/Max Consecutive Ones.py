class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                if current > max_ones:
                    max_ones = current
            else:
                current = 0
                
        return max_ones
