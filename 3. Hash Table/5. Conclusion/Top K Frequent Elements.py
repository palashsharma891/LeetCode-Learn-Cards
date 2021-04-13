class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1
                
        vals = sorted(list(num_map.values()), reverse=True)[:k]
        ans = []
        
        for key in num_map.keys():
            if num_map[key] in vals:
                ans += [key]
                
        return ans
