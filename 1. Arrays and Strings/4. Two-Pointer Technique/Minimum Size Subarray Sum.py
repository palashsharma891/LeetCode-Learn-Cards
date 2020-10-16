class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        result = len(nums)
        left = 0
        val_sum = 0
        flag = 0
        
        for i in range(len(nums)):
            
            val_sum += nums[i]
            
            while(val_sum >= s):
                result = min(result, i + 1 - left)
                val_sum -= nums[left]
                left += 1
                flag = 1
                
        if flag:
            return result
        else:
            return 0
        
#        min_len = len(nums)
#        i = -1
#        f = 0
#        
#        while i < len(nums)-1:
#            i += 1
#            sub_sum = 0
#            for j in range(i, len(nums)):
#                sub_sum += nums[j]
#                if sub_sum >= s:
#                    if min_len >= j - i + 1:
#                        min_len = j-i+1
#                        f = 1
#                    break
#                    
#            #print(min_len)
#        
#        if not f:
#            return 0
#        else:
#            return min_len
