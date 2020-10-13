class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        for i in nums:
            if i != max_num and max_num < 2*i:
                return -1
            
        return nums.index(max_num)
