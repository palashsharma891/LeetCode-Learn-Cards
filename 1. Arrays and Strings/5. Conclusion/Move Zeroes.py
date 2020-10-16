class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[k] = nums[i]
                k += 1
                
        while k < len(nums):
            nums[k] = 0
            k += 1
        
#        zeros = 0
#        nums_copy = nums[:]
#        for i in range(len(nums_copy)):
#            if nums_copy[i] == 0:
#                nums.pop(i-zeros)
#                #print(nums)
#                zeros += 1
#                
#       nums += [0] * zeros
