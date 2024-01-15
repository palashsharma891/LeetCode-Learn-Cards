class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def digits(n):
            d = 0
            while n > 0:
                d += 1
                n = n // 10
            return d
        ans = 0
        for n in nums:
            if digits(n) % 2 == 0:
                ans += 1
                
        return ans
