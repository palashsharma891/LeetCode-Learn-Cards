class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        f = len(nums)-1
        l, r = 0, len(nums)-1
        while f >= 0:
            if abs(nums[l]) > abs(nums[r]):
                ans[f] = nums[l]**2
                l += 1
            else:
                ans[f] = nums[r]**2
                r -= 1
            f -= 1
        return ans
