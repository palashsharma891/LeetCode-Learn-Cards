class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        ans = 0
        while r < len(nums):
            curr_max = 0
            while r < len(nums) and nums[r] == 1:
                curr_max += 1
                r += 1
            ans = max(curr_max, ans)
            r += 1
        return ans

# OR

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                if c > max_ones:
                    max_ones = c
                c = 0
        return max(max_ones, c) #double check required in this case, so solution above is better. TC/SC is same.

# double check is required because the maximum consecutive ones can appear at the end of the list which would result in the else clause never being executed!
