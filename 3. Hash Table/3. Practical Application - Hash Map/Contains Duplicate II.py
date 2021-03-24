class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        num_map = {}
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = [i]
            else:
                num_map[nums[i]] += [i]
                
        print(num_map)
                
        for num in num_map:
            if len(num_map[num]) > 1:
                for i in range(len(num_map[num])-1):
                    if abs(num_map[num][i] - num_map[num][i+1]) <= k:
                        return True
                
        return False
