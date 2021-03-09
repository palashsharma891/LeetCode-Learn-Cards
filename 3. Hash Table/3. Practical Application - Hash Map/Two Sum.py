class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in num_dict:
                num_dict[num] = i
            else:
                return [num_dict[n], i]
