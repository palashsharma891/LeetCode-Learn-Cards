class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        num_list = []
        
        for i in range(0, len(nums), 2):
            num_list += [[nums[i], nums[i+1]]]
        
        sum_list = 0
        for i in range(len(num_list)):
            sum_list += min(num_list[i])
            
        return sum_list
