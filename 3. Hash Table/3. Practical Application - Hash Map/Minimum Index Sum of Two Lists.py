class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        hash1, hash2 = {}, {}
        for i in range(len(list1)):
            hash1[list1[i]] = i
        for i in range(len(list2)):
            hash2[list2[i]] = i
        
        ans, min_sum = [], 2002
        for key in hash1:
            if key in hash2:
                ind_sum = hash1[key] + hash2[key]
                if ind_sum < min_sum:
                    min_sum = ind_sum
                    ans = [key]
                elif ind_sum == min_sum:
                    ans += [key]
                    
        return ans
